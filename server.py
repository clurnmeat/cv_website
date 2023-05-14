from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/About-Me")
def aboutMe():
    return render_template("aboutMe.html")


if __name__ == "__main__":
    import gevent.pywsgi
    app_server = gevent.pywsgi.WSGIServer(('localhost', 8080), app)
    print('jammin on 8080')

if __name__ == "__main__":
    import gevent.pywsgi
    app_server = gevent.pywsgi.WSGIServer(('localhost', 80), app)
    app_server.serve_forever()
