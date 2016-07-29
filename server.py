from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def show_user_profile():
	return render_template('user.html')

@app.route('/back')
def back():
	return redirect('/')

@app.route('/show', methods=['POST'])
def show():
	username = request.form['username']
	if username == "blue" or username == "Blue":
		return render_template("show.html", username=username)
	if username == "orange" or username == "Orange":
		return render_template("show.html", username=username)
	if username == "purple" or username == "Purple":
		return render_template("show.html", username=username)
	if username == "red" or username == "Red":
		return render_template("show.html", username=username)
	if username == "ninja" or username == "Ninja":
		return render_template("show.html", username=username)
	if username == "april" or username == "April":
		return render_template("show.html", username=username)
	else:
		return render_template("none.html", username=username)

app.run(debug=True)