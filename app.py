from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Femgineering Dashboard</h1><p>It's alive.</p>"

if __name__ == "__main__":
    app.run(debug=True)
