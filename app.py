from flask import Flask, render_template

app = Flask(__name__)

topics = [
    {"name": "Menopause", "why_it_matters": "Still under-researched and often dismissed by clinicians."},
    {"name": "Endometriosis", "why_it_matters": "Takes years to diagnose despite affecting 1 in 10 women."},
    {"name": "Post Partum Care", "why_it_matters": "The U.S has the worst maternal mortality rate of any developed nation and the number one cause of maternal death in the U.S is suicide."}
 ]

@app.route("/")
def home():
    return "<h1>Femgineering Dashboard</h1><p>It's alive.</p>"

@app.route("/about")
def about ():
	return "<h1>About Femgineering Health</h1><p>Hey, welcome to Femgineering! I’m Amanda. This show is for engineers, curious minds, and anyone who believes women deserve better healthcare. We’re diving into the gaps in women’s health, exploring the female body, and dreaming up what’s next. Let’s get into it. </p> "

@app.route("/topics")
def topics_page():
    return render_template("topics.html", topics=topics)

if __name__ == "__main__":
    app.run(debug=True)
 
