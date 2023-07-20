from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

username = "nittai"
password = "1234"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]

@app.route('/friend_exists/<string:friend>')
def friend_exists_route(friend): 
    return render_template('friend_exists.html', friend = friend)

@app.route('/home')
def home():
	return render_template('home.html', facebook_friends = facebook_friends)
                                          


@app.route('/', methods=["GET", "POST"])  # '/' for the default page
def login():
  if request.method == "GET":
  	return render_template('login.html')
  else:
  	html_name = request.form['username']
  	html_password = request.form['password']
  	if (username == html_name and password == html_password):
  		return redirect(url_for('home'))
  	else:
  		return render_template('login.html')


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)

