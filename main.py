from flask import Flask
app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
  
    
@app.route('/')
def hello():
    return "welcome to the flask tutorials"
  
  
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 