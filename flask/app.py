from flask import Flask, jsonify, redirect, render_template, session, url_for, request, json
from authlib.flask.client import OAuth
from functools import wraps
from decouple import config
from six.moves.urllib.parse import urlencode
from models import DB, User
from werkzeug.exceptions import BadRequestKeyError

app = Flask(__name__)
app.secret_key = config("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = config("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
DB.init_app(app)
oauth = OAuth(app)

auth0 = oauth.register(
    "auth0",
    client_id=config("CLIENT_ID"),
    client_secret=config("CLIENT_SECRET"),
    api_base_url=config("API_BASE_URL"),
    authorize_url=config("AUTHORIZE_URL"),
    access_token_url =config("ACCESS_TOKEN_URL"),
    client_kwargs={"scope": "openid profile",},
)


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "profile" not in session:
            return redirect("/")
        return f(*args, **kwargs)

    return decorated


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/new_task", methods=["POST"])
def create_new_task():
    #import pdb;pdb.set_trace()
    new_task = {}
    new_task["task_name"] = request.values["task_name"]
    new_task["task_description"] = request.values["task_description"]
    new_task["task_start_hour"] = request.values["task_start_hour"]
    new_task["task_start_minutes"] = request.values["task_start_minutes"]
    new_task["task_end_hour"] = request.values["task_end_hour"]
    new_task["task_end_minutes"] = request.values["task_end_minutes"]
    new_task["task_interval"] = request.values["task_interval"]
    
    for i in ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]:
        try:
            t = f'task_{i}'
            if request.values[t] =="on":
                new_task[t] = True
        except BadRequestKeyError:
            new_task[t] = False

    # try:
    #     if request.values["task_Monday"] == "on":
    #     new_task["task_Monday"] = True
    # except werkzeug.exceptions.BadRequestKeyError:
    #     new_task["task_Monday"] = False
    


    return jsonify(new_task)

@app.route("/callback")
def callback_handling():
    auth0.authorize_access_token()
    resp = auth0.get("userinfo")
    userinfo = resp.json()

    session["jwt_payload"] = userinfo
    session["profile"] = {
        "user_id": userinfo["sub"],
        "name": userinfo["name"],
    }
    db_user = User.query.get(userinfo["sub"]) or User(
        id=userinfo["sub"], name=userinfo["name"]
    )
    DB.session.add(db_user)
    DB.session.commit()
    return redirect("/dashboard")


@app.route("/login")
def login():
    return auth0.authorize_redirect(
        redirect_uri="http://127.0.0.1:5000/callback",
        audience="https://crawftv.auth0.com/userinfo",
    )


@app.route("/dashboard")
@requires_auth
def dashboard():
    userinfo=session["profile"],
    userinfo_pretty=json.dumps(session["jwt_payload"], indent=4),
    return render_template(
        "dashboard.html",userinfo=userinfo, userinfo_pretty=userinfo_pretty,
    )


@app.route("/logout")
@requires_auth
def logout():
    session.clear()
    params = {
        "returnTo": url_for("home", _external=True),
        "client_id": config("CLIENT_ID"),
    }
    return redirect(auth0.api_base_url + "/v2/logout?" + urlencode(params))


if __name__ == "__main__":
    app.run()
