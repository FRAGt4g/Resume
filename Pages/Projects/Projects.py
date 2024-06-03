from flask import Flask, Blueprint, render_template, send_from_directory, current_app, url_for

projects_bp = Blueprint('Projects', __name__, template_folder='./HTML', static_folder='../Projects')

@projects_bp.route('/')
def root():
  return render_template('Contact.html', bp_adress='Projects') 