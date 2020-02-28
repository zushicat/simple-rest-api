### Description
A very simple API using werkzeug and jsrpc
- when running docker container, in Dockerfile
CMD ["poetry", "run", "python", "-m", "simple_rest_api.api"]:
  - starts service in src/api/_main_.py
  - src/api/server.py: function "application" waits for jsrpc request
  - on request: dispatcher delegates to src/fancy_stuff/_my_application.py
      - passing the attributes from "params" in request
      - a file in /data is read, getting the attribute "name"
      - both values are passed to do_something in _make_fancy_shit
          - returns json
      - returns returned json
  - returns API response

No additional fancyness (such as logging, testing & stuff) implemented.

### Prerequisite
- install latest version of docker

### If you are using Visual Studio Code
- (If you are using OSX, install with brew cask install visual-studio-code)
- Useful Extensions: Python, REST Client
- If you want to use REST Client (recommended):
    - Create file with extension .http (i.e. test_request.http)
    - Copy request text from below into file
    - "Send Request" will appear in file: click to request (tab with response will open)


### Start Docker Container
Build and run docker container (with exposed port) named "api_cradle"
```
docker build -t simple_rest_api .
docker run -p 8080:80 simple_rest_api
```

Or if you like like to reload after changes while container is running:
```
docker run --rm -it -p 8080:80 -v $(pwd):/app simple_rest_api
```

### request
2 example request methods implemented:

1) mytestrequest
with curl
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"jsonrpc":"2.0","id":12345,"method":"mytestrequest","params":{}}' \
  http://localhost:8080
```
or with REST Client extension for Visual Studio (see below)
```
POST http://localhost:8080
Content-Type: application/json

{
    "jsonrpc": "2.0",
    "id": 12345,
    "method": "mytestrequest",
    "params": {}
}
```

returns
```
{
  "result": {
    "status": "YAY! API is running."
  },
  "id": 12345,
  "jsonrpc": "2.0"
}
```

2) myfancyendpoint.fancyrequest
pass parameter "stuff" by http request
with curl
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"jsonrpc":"2.0","id":12345,"method":"myfancyendpoint.fancyrequest","params":{"stuff":"Foo Stuff"}}' \
  http://localhost:8080
```
or with REST Client extension for Visual Studio (see below)
```
POST http://localhost:8080
Content-Type: application/json

{
    "jsonrpc": "2.0",
    "id": 12345,
    "method": "myfancyendpoint.fancyrequest",
    "params": {"stuff": "Foo Stuff"}
}
```

returns
```
{
  "result": {
    "status": "YAY!",
    "name from file": "Fuzzy Bear",
    "name from request": "Foo Stuff",
    "date": "2019-06-05 13:57:46.333072"
  },
  "id": 12345,
  "jsonrpc": "2.0"
}
```