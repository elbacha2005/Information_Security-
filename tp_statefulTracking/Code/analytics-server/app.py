from flask import Flask, request, make_response
import secrets

app = Flask(__name__)

COOKIE_NAME = "_analytics_id"

collected_data = []

# 1x1 transparent GIF
PIXEL = (
    b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff"
    b"\x00\x00\x00\x21\xf9\x04\x00\x00\x00\x00\x00\x2c\x00\x00\x00\x00"
    b"\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b"
)


@app.route("/collect")
def collect():
    # This server's own cookie is the authoritative cross-site ID: it lives on
    # analytics.loc, so it is the same value on every publisher page. The uid in
    # the query string is only the per-publisher fallback that analytics.js set.
    uid = request.cookies.get(COOKIE_NAME)
    is_new = uid is None
    if is_new:
        uid = request.args.get("uid") or secrets.token_hex(8)

    entry = {
        "uid": uid,
        "source": "query" if is_new else "cookie",
        "url": request.args.get("url"),
        "title": request.args.get("title"),
        "referrer": request.args.get("referrer"),
        "timestamp": request.args.get("timestamp"),
    }
    collected_data.append(entry)

    print(
        f"--- ANALYTICS COLLECT (#{len(collected_data)}) ---\n"
        f"  [{entry['timestamp']}] UID={entry['uid']} ({entry['source']})\n"
        f"  url={entry['url']}\n"
        f"  title={entry['title']}\n"
        f"  referrer={entry['referrer']}",
        flush=True,
    )

    response = make_response(PIXEL)
    response.headers["Content-Type"] = "image/gif"
    # Never let a proxy or the browser serve this beacon from cache.
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"

    if is_new:
        # SameSite=None is required for the cookie to ride along on a third-party
        # image request. Browsers also demand Secure for SameSite=None, so over
        # plain HTTP this is set on a best-effort basis only.
        response.set_cookie(
            COOKIE_NAME, uid, max_age=31536000, samesite="None", secure=False
        )

    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9100, debug=True)
