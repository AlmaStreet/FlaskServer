# FlaskServer
This project demonstrates System Design principles being implemented

Every time the /robin route (or endpoint) is requested on the Load Balancer Server, the Load Balancer will send a get request to either WebServer1 or WebServer2. The webservers then respond with data counting the amount of times traffic was routed there. This response data is then displayed on the Load Balance Server.

To run this project:
1. Make sure you have flask and requests installed.

```
pip install flask
pip install requests
```
2. Run LoadBalancer.py
3. Run WebServer1.py
4. Run WebServer2.py
5. In your browser, type:
```http://127.0.0.1:5000/api/balance```
6. You can keep refreshing the page to see which webserver is being used and how many times each webserver was accessed.
