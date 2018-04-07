from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect

from src.models.users.user import User
import src.models.users.errors as UserError

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.is_valid_login(email, password):
                session["email"] = email
                return redirect(url_for(".user_alerts"))
        except UserError.UserError as e:
            return e.message

    return render_template("users/login.html")


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for('.user_alerts'))
        except UserError.UserError as e:
            return e.message

    return render_template("users/register.html")


@user_blueprint.route("/alerts")
def user_alerts():
    return "This is the Alerts Page"


@user_blueprint.route("/logout")
def logout_user():
    pass


@user_blueprint.route("/check_alerts/<string:user_id>")
def check_user_alert(user_id):
    pass
