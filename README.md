# http testing

A CORS-enabled Flask app for testing http responses.

`curl -X PUT http://localhost:8888/403`

```

* Connected to localhost (127.0.0.1) port 8888 (#0)
* > PUT /403 HTTP/1.1
* > User-Agent: curl/7.38.0
* > Host: localhost:8888
* > Accept: */*
* >
* * HTTP 1.0, assume close after body
* < HTTP/1.0 403 FORBIDDEN
* < Content-Type: application/json
* < Content-Length: 2
* < Access-Control-Allow-Origin: *
* < Server: Werkzeug/0.11.2 Python/2.7.9
* < Date: Mon, 14 Dec 2015 19:58:55 GMT
* <
* * Closing connection 0
* {}%

```

