from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    import datetime
    date = datetime.date.today()
    date_update = date.isoformat()
    return render_template("index.html", date=date_update[0:4])






if __name__ == "__main__":
    import gevent.pywsgi
    app_server = gevent.pywsgi.WSGIServer(('localhost', 8080), app)
    app_server.serve_forever()
    print('jammin on 8080')
