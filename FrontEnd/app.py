from flask import Flask
from flask import render_template,redirect,request

app=Flask(__name__)

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/home',methods=['POST'])
def data():
	text=request.form['text']
	f = open("../app/data/test.txt", "a")
	f.write(text+"\n")
	f.close()
	return text
'''
def hello_world():
	f = open("../app/data/test.txt", "w")
	f.write("Woops! I have deleted the content!")
	f.close()
	return 'Flask Dockerized'
'''
if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')
