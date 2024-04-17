from flask import Flask, Blueprint, render_template, send_from_directory, current_app, url_for

contact_bp = Blueprint('Contact', __name__, template_folder='./HTML', static_folder='../Contact')

@contact_bp.route('/')
def root():
  return render_template('Contact.html', bp_adress='Contact') 