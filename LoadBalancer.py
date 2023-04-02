from flask import Flask
import requests

app = Flask(__name__)

available_servers = 2
incoming_traffic = 0


@app.route('/')
def root():
    return 'Hello, World! - Load Balancer'


@app.route('/robin')
def round_robin():
    # routing traffic with Round Robin
    global incoming_traffic
    incoming_traffic += 1
    traffic_route = incoming_traffic % available_servers

    # call either WS1 or WS2
    if traffic_route == 1:
        response = requests.get('http://127.0.0.1:5000/api/balance')
    else:
        response = requests.get('http://127.0.0.1:5001/api/balance')

    print(response.text)
    # return result WS1 or WS2
    return f'response_data is {response.json()}'


if __name__ == "__main__":
    app.run(port=5002)
