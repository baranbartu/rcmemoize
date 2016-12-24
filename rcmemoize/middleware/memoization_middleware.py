from rcmemoize.request import request_context
from rcmemoize.memoization import memoization_registry


class RequestCycleMemoizationMiddleware(object):
    # can be cached anything in memory for only current request cycle
    def process_request(self, request):
        request_id = request_context.set_request(request)
        memoization_registry.create_bucket(request_id)

    def process_response(self, request, response):
        memoization_registry.delete_bucket(
            request_context.get_request_id(request))
        request_context.delete_request()
        return response
