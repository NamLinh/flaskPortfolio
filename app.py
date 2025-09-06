from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    projects_list = [
        {"name": "Portfolio Website", "url": "https://github.com/yourusername/portfolio"},
        {"name": "Boba Shop Simulator Game", "url": "https://github.com/NamLinh/bobaShopSim"},
        {"name": "Friend Group Mental Health Analyser (Sentiment Analysis)", "url": "https://github.com/NamLinh/discSentAnalysis"},
    ]
    return render_template("projects.html", projects=projects_list)

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)


