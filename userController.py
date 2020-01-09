from flask import Blueprint

user_api = Blueprint('user_api', __name__)

@user_api.route("/user")
def users():
    return "list of users"