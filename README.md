### Description
A very simple API using werkzeug and jsrpc
- when running docker container, in Dockerfile
CMD ["poetry", "run", "python", "-m", "api_cradle.api"]:
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
- (maybe: docker --> preferences --> allowcate more memory)

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
docker build -t api_cradle .
docker run -p 8080:80 api_cradle
```

### request
2 request methods implemented:

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

2) cradle.fancyrequest
pass parameter "stuff" by http request
with curl
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"jsonrpc":"2.0","id":12345,"method":"cradle.fancyrequest","params":{"stuff":"Foo Stuff"}}' \
  http://localhost:8080
```
or with REST Client extension for Visual Studio (see below)
```
POST http://localhost:8080
Content-Type: application/json

{
    "jsonrpc": "2.0",
    "id": 12345,
    "method": "cradle.fancyrequest",
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