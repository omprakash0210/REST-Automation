from flask import Flask

# the all-important app variable:
app = Flask(__name__)


@app.route("/", methods=['GET'])
def launch():
    return "Oh, Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
