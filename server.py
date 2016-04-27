from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def show_user_profile():
	return render_template('user.html')

@app.route('/show', methods=['POST'])
def show():
	username = request.form['username']
	if username == "Blue":
		return render_template("show.html", username=username)
	if username == "Orange":
		return render_template("show.html", username=username)
	if username == "Purple":
		return render_template("show.html", username=username)
	if username == "Red":
		return render_template("show.html", username=username)
	if username == "Ninja":
		return render_template("show.html", username=username)
	else:
		return render_template("show.html", username="april")

app.run(debug=True)