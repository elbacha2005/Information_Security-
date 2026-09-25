from flask import Flask, render_template, request, make_response
import secrets

app = Flask(__name__)

@app.route("/")
def home():
    # check if the browser already has an identifier cookie
    aid = request.cookies.get("aid")
    is_new = aid is None

    # create a new identifier is the user does not have one 
    if is_new:
        aid = secrets.token_hex(8)

    # the normale HTTP reponse containing the index.html
    # we use this function to make customizations to the response, such as setting cookies
    response = make_response(render_template("index.html"))

    # ask the browser to store the cookie 
    if is_new:
        response.set_cookie(key="aid", value=aid, max_age=60, samesite="Strict")

    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)