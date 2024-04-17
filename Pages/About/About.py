from flask import Flask, Blueprint, render_template, send_from_directory, current_app, url_for

about_bp = Blueprint('About', __name__, template_folder='./HTML', static_folder='../About')

@about_bp.route('/')
def root():
  return render_template('About.html', bp_adress='About')