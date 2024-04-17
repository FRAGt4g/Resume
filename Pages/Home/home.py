from flask import Flask, Blueprint, render_template, send_from_directory, current_app, url_for

home_bp = Blueprint('Home', __name__, template_folder='./HTML', static_folder='../Home')

@home_bp.route('/')
def root():
    return render_template('Home.html', bp_adress='Home')