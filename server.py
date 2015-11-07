from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route(/)
def index():
	return render_template('index.html')
@app.route(/ninja)
def turtles():
	return render_template('ninjas.html')
@app.route(/ninja/<color>)
def ninja(color):
	if color == 'blue':
		return render_template('blue.html')
	elif color == 'orange':
		return render_template('orange.html')
	elif color == 'purple':
		return render_template('purple.html')
	elif color == 'red':
		return render_template('red.html')
	else:
		return render_template('fox.html')

#four color options


app.run(debug=True)