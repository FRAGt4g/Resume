from flask import Flask, render_template, send_from_directory, url_for, redirect, request

from Pages.Home.home import home_bp
from Pages.About.About import about_bp
from Pages.Contact.Contact import contact_bp

app = Flask(__name__, template_folder='Universal/HTML')

app.register_blueprint(home_bp, url_prefix='/Home')
app.register_blueprint(about_bp, url_prefix='/About')
app.register_blueprint(contact_bp, url_prefix='/Contact')


@app.route('/')
def route_to_main():
    return redirect('/Home')

#Used to route to css folder within each blueprint
@app.route('/CSS/<bp>/<filename>')
def css(bp, filename):
    return send_from_directory('Pages/' + bp + '/css', filename)

#Used to route to javascript folder within each blueprint
@app.route('/JS/<bp>/<filename>')
def js(bp, filename):
    return send_from_directory('Pages/' + bp + '/js', filename)

if __name__ == '__main__':
    app.run(debug=True)