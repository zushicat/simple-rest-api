import json
from typing import Any, Callable

from jsonrpc import JSONRPCResponseManager, dispatcher
from jsonrpc.exceptions import JSONRPCDispatchException
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException

from .exceptions import InternalError
from simple_rest_api.fancy_stuff import give_result, test_request


def http_exception(req: Request, e: HTTPException) -> Response:
    return Response(
        json.dumps({"status": f"ERROR: {e.description}"}).encode(),
        content_type="application/json",
        status=e.code,
    )


def json_rpc_except(func: Callable) -> Callable:
    def func_wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(**kwargs)
        except JSONRPCDispatchException:
            raise
        except Exception as e:
            raise InternalError(f"INTERNAL ERROR: {e}")

    return func_wrapper


@Request.application
def application(request):
    try:
        dispatcher['myfancyendpoint.fancyrequest'] = json_rpc_except(give_result)
        dispatcher['mytestrequest'] = json_rpc_except(test_request)
        response = JSONRPCResponseManager.handle(request.data, dispatcher)
        return (Response(response.json, mimetype='application/json'))
    except Exception as e:
        return Response(
            json.dumps({"status": f"ERROR: {e}"}).encode(),
            content_type="application/json",
        )
    except HTTPException as e:
        return http_exception(request, e)
