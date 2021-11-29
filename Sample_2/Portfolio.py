from flask import Flask, render_template
aiml = Flask(__name__)

list_of_projects = [
    'Mad Libs Generator',
    'Number Guessing',
    'Text-based Adventure Game',
    'Dice Rolling Simulator',
    'Hangman',
    'Contact Book',
    'Email Slicer',
    'Binary search algorithm',
    'Desktop Notifier App',
    'Python Story Generator',
    'YouTube video downloader',
    'Python Website Blocker',
    'Spin a Yarn',
    'What’s the word',
    'Rock, Paper, Scissors',
    'Leap it!',
    'Find out, Fibonacci!',
    'Calculator',
    'Countdown Clock and Timer',
    'Random Password Generator',
    'Random Wikipedia Article',
    'Reddit Bot',
    'Python Command-Line Application',
    'Alarm Clock',
    'Tic-Tac-Toe',
    'Steganography',
    'Currency converter',
    'Post-it Notes',
    'Site Connectivity Checker',
    'Directory Tree Generator',
    'Speed Typing Test',
    'Content Aggregator',
    'Bulk File Rename/ Image Resize Application',
    'Python File Explorer',
    'Plagiarism Checker',
    'Web Crawler',
    'Music Player',
    'Price Comparison Extension',
    'Expense Tracker',
    'Regex Query Tool',
    'Instagram Photo Downloader',
    'Quiz Application'
]



@aiml.route("/")
@aiml.route("/home")
def home():
    return render_template("home.html", t_home="BlueSky_Home")

@aiml.route("/about me")
def about():
    return render_template("about me.html", t_about="about BlueSky")

@aiml.route("/projects")
def projects():
    return render_template("projects.html", t_project="BlueSky Projects", l_pro = list_of_projects, len_list=len(list_of_projects))

@aiml.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    aiml.run(debug=True)
