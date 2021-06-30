from flask import (
    Blueprint, flash, g, redirect, request, session, url_for, render_template
)
from werkzeug.security import check_password_hash, generate_password_hash

fe = Blueprint('fe', __name__, url_prefix='/admin',
               template_folder="templates", static_folder='static')


@fe.route('/')
def admin():
    return redirect(url_for('fe.dashboard'))


@fe.route('/dashboard')
def dashboard():
    return render_template('index.html', title="Index hello")
