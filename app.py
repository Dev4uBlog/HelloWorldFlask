from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True, port= 5000)