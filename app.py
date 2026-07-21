from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Femgineering Dashboard</h1><p>It's alive.</p>"

@app.route("/about")
def about ():
	return "<h1>About Femgineering Health</h1><p>Hey, welcome to Femgineering! I’m Amanda. This show is for engineers, curious minds, and anyone who believes women deserve better healthcare. We’re diving into the gaps in women’s health, exploring the female body, and dreaming up what’s next. Let’s get into it. </p> "

if __name__ == "__main__":
    app.run(debug=True)
 
