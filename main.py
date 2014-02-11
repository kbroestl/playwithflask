from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	# Next step -- how do we implement models?
	# how do we get variables from one place in the
	# app to the next?
	return render_template('hello.html')

if __name__ == "__main__":
	app.run()