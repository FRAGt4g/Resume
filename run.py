from flask import Flask, render_template, send_from_directory, url_for, redirect, request

from Pages.Home.home import home_bp
from Pages.About.About import about_bp
from Pages.Contact.Contact import contact_bp
from Pages.Projects.Projects import projects_bp

app = Flask(__name__, template_folder='Universal/HTML')

app.register_blueprint(home_bp, url_prefix='/Home')
app.register_blueprint(about_bp, url_prefix='/About')
app.register_blueprint(contact_bp, url_prefix='/Contact')
app.register_blueprint(projects_bp, url_prefix='/Projects')


@app.route('/')
def route_to_main():
    return redirect('/Home')

#Used to route to Universal folder
@app.route('/Universal/CSS/<filename>')
def universal_css(filename):
    print(filename)
    file = send_from_directory('Universal/CSS', filename)
    print(str(file.content_type))
    return file

#Used to route to Universal folder
@app.route('/Universal/HTML/<filename>')
def universal_html(filename):
    return send_from_directory('Universal/HTML', filename)

#Used to route to css folder within each blueprint
@app.route('/CSS/<bp>/<filename>')
def css(bp, filename):
    return send_from_directory('Pages/' + bp + '/css', filename)

@app.route('/Downloads/<filename>')
def downloads(filename):
    return send_from_directory('Downloads/', filename)

#Used to route to javascript folder within each blueprint
@app.route('/JS/<bp>/<filename>')
def js(bp, filename):
    return send_from_directory('Pages/' + bp + '/js', filename)

if __name__ == '__main__':
    app.run(debug=True)