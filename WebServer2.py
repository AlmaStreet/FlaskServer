from flask import Flask

app = Flask(__name__)

serverName = "WebServer"
serverNumber = 2
count = 0


@app.route('/')
def root():
    return f'Welcome to {serverName} {serverNumber}!'


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/home')
def home():
    return root()


@app.route('/contact')
def contact():
    return 'Contact me at jason.jia.chen@gmail.com'


@app.route('/about')
def about():
    return f'This is {serverName} {serverNumber}. I am younger than WS 1!'


@app.route('/api/square/<int:num>')
def square(num):
    result = num * num
    return {'input': num, 'result': result}


@app.route('/api/balance', methods=['GET'])
def balance():
    global count
    count += 1
    return {'serverName': serverName, 'serverNumber': serverNumber, 'count': count}


if __name__ == '__main__':
    app.run(port=5001)
