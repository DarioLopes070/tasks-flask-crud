from flask import Flask

"""__name__ = __main__"""
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"
@app.route("/about")
def about():
    return "Página sobre"

if(__name__ == "__main__"):
    app.run(debug=True, port=8080)

# from flask import Flask 

# app = Flask(__name__) 

# # Pass the required route to the decorator. 
# @app.route("/hello") 
# def hello(): 
# 	return "Hello, Welcome to GeeksForGeeks"
	
# @app.route("/") 
# def index(): 
# 	return "Homepage of GeeksForGeeks"

# if __name__ == "__main__": 
# 	app.run(debug=True, port=8080) 
