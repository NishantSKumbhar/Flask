from flask import Flask, render_template
ai = Flask(__name__)

@ai.route("/")
@ai.route("/home")
def home():
	return render_template("home.html")

@ai.route("/about")
def about():
	return render_template("about.html")

@ai.route("/contact")
@ai.route("/need_help")
def contact():
	return render_template("contact.html")

if __name__ == '__main__':
	ai.run(debug=True)

