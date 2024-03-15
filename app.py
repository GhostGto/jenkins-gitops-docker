from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask is running in a Docker container! webhook test'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
