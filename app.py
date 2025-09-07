from flask import Flask, render_template, request, redirect, flash
import os
from flask_mail import Mail, Message

rand_int = os.urandom(24)

app = Flask(__name__)
app.secret_key = rand_int

# -----------------------
# Flask-Mail Configuration
# -----------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'namlinhduong2@gmail.com'    
app.config['MAIL_PASSWORD'] = 'gdri fapv bxlw spaa'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/todo")
def todo():
    return render_template("todo.html")

@app.route("/projects")

def projects():
    projects_list = [
        {"name": "Portfolio Website", "url": "https://github.com/NamLinh/flaskPortfolio"},
        {"name": "Friend Group Mental Health Analyser (Sentiment Analysis)", "url": "https://github.com/NamLinh/discSentAnalysis"},
        {"name": "Boba Shop Simulator", "url": "https://github.com/NamLinh/bobaShopSim"},
    ]
    return render_template("projects.html", projects=projects_list)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        message_body = request.form.get("message")
        mail = Mail(app)

        # Create email message
        msg = Message(
            subject=f"New message from {name}",
            sender=app.config['MAIL_USERNAME'],        
            recipients=[app.config['MAIL_USERNAME']],
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}",
            reply_to=email                         
        )

        # Send the email
        try:
            mail.send(msg)
            flash("Thank you! Your message has been sent.", "success")
        except Exception as e:
            print("Mail sending failed:", e)
            flash("Oops! Something went wrong. Try again later.", "danger")

        return redirect("/contact")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)


