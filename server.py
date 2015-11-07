from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route(/)
def index():
	print "No ninjas here"
@app.route(/ninja)
@app.route(/ninja/<color>)
def ninja(color):

#four color options
@app.route(/ninja/)

app.run(debug=True)