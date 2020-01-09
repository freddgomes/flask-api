from flask import Flask
from userController import user_api
from accountController import account_api

app = Flask(__name__)

app.register_blueprint(user_api)
app.register_blueprint(account_api)

@app.route("/")
def default():
    return "default"

if __name__ == "__main__":
    app.run()