from flask import Flask
import model

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Sever is working'



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)