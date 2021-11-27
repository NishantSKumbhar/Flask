from flask import Flask
ai = Flask(__name__)

@ai.route("/")
@ai.route("/home")
def home():
	return "Hi"

@ai.route("/about")
def about():
	return "This is a About Section."

@ai.route("/contact")
@ai.route("/need_help")
def contact():
	return "This is Contact Section, it will return list of phone numbers."

if __name__ == '__main__':
	ai.run(debug=True)

