from flask import Blueprint

account_api = Blueprint('account_api', __name__)

@account_api.route("/account")
def accounts():
    return "list of accounts"

@account_api.route("/account/<int:id>")
def account(id):

    return "account " + str(id)