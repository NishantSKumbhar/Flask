from flask import Flask, render_template
ai = Flask(__name__)

list_of_specs = [
	{
	'company' : 'Apple',
	'color' : 'Product Red',
	'model' : 'iphone xR',
	'price' : 40000,
	'if_donate' : True
	},
	{
	'company' : 'Apple',
	'color' : 'Purple',
	'model' : 'iphone 12 mini',
	'price' : 50000,
	'if_donate' : False
	}

]

list_of_employee = [
	{
	'name' : 'Mark',
	'profile' : 'tech-lid',
	'ph_number' : 9865857546
	},
	{
	'name' : 'Sara',
	'profile' : 'P.A',
	'ph_number' : 7845986526
	}
]
# if yo define list below the respective function then it wil give error that they are not found.
@ai.route("/")
@ai.route("/home")
def home():
	return render_template("home.html", specs = list_of_specs)

@ai.route("/about")
def about():
	return render_template("about.html", empl = list_of_employee)

@ai.route("/contact")
@ai.route("/need_help")
def contact():
	return render_template("contact.html", empl = list_of_employee)

if __name__ == '__main__':
	ai.run(debug=True)

