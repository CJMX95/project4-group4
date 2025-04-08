from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
# Get the directory where the current script is located
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# Set the template folder to be in the same directory as the script
app.template_folder = APP_ROOT

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/tableau')
def tableau():
    return render_template('tableau.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/works_cited')
def works_cited():
    return render_template('Works Cited.html')

@app.route('/<filename>')
def serve_static(filename):
    """Serve static files (CSS, images, etc.)"""
    return send_from_directory(APP_ROOT, filename)

if __name__ == '__main__':
    app.run(debug=True)
