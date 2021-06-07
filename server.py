from flask import Flask, send_from_directory
app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello World!"
@app.route("/")
def home():
    return send_from_directory('Website', 'index.html')

@app.route("/vickis_vision/")
def vicki_home():
    return send_from_directory('vickis_vision', 'index.html')

@app.route('/vickis_vision/<path:path>')
def vicki_static_file(path):
    print("Query path:", path)
    return send_from_directory("vickis_vision", path)

@app.route('/<path:path>')
def static_file(path):
    print("Query path:", path)
    return send_from_directory("Website", path)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)