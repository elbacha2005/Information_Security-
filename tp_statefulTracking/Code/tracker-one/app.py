from flask import Flask, render_template, request, make_response
import secrets
from datetime import datetime

app = Flask(__name__)

# In-memory log of all tracking events
profile_log = []

@app.route("/track")
def track():
    # Read or create the tracking cookie
    tid = request.cookies.get("tid")
    is_new = tid is None
    if is_new:
        tid = secrets.token_hex(8)

    publisher = request.args.get("publisher", "unknown")
    page = request.args.get("page", "unknown")

    # Log the visit
    profile_log.append({
        "tid": tid,
        "publisher": publisher,
        "page": page,
        "time": datetime.now().isoformat()
    })

    print(f"\n--- TRACKER LOG ---")
    for entry in profile_log:
        print(f"  [{entry['time']}] ID={entry['tid']} | {entry['publisher']} | {entry['page']}")

    response = make_response(render_template("index.html"))

    if is_new:
        response.set_cookie("tid", tid, samesite="None", secure=False)

    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True)