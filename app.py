from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'My name is Onwukanjo Innocent, and this Page shows that my flask app is running. Thanks'

if __name__ == "__main__":    
    app.run(host='0.0.0.0', port=80, debug=True) #specify port=80