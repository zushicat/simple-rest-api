import datetime
from typing import Any, Dict

# ********************************
# called from _my_application:
# do something and return json response
# ********************************
def do_something(some_string_from_file: str, stuff_from_request: str) -> Dict[str, Any]:
    try:
        response: Dict[str, str] = {
            "status": "YAY! It works!",
            "name from file": some_string_from_file,
            "name from request": stuff_from_request,
            "date": f"{datetime.datetime.now()}"
        }
        return response
    except Exception as e:
        return {"status": f"Nooooo! Something went wrong. {e}"}
