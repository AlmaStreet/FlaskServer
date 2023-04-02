# FlaskServer
This project demonstrates System Design principles being implemented

Every time the /robin route (or endpoint) is requested on the Load Balancer Server, the Load Balancer will send a get request to either WebServer1 or WebServer2. The webservers then respond with data counting the amount of times traffic was routed there. This response data is then displayed on the Load Balance Server.
