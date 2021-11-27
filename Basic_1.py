from flask import Flask
ai = Flask(__name__)

@ai.route("/")
@ai.route("/home")
def home():
	return "Hi"



if __name__ == '__main__':
	ai.run(debug=True)

