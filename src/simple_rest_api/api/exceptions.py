from typing import Any

from jsonrpc.exceptions import JSONRPCDispatchException

# ***************************
# something went wrong internally
# ***************************
class InternalError(JSONRPCDispatchException):
    def __init__(self, message: str, data: Any=None) -> None:
        super(InternalError, self).__init__(code=1, data=data, message=message)

# ***************************
# supplied parameters are wrong
# ***************************
class InvalidRequest(JSONRPCDispatchException):
    def __init__(self, message: str, data: Any=None) -> None:
        super(InvalidRequest, self).__init__(code=2, data=data, message=message)
