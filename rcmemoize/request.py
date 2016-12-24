import uuid
from threading import current_thread


class RequestContext(object):
    def __init__(self):
        self.registry = {}

    def set_request(self, request):
        request_id = str(uuid.uuid4())
        setattr(request, 'request_id', request_id)
        self.registry[current_thread()] = request
        return request_id

    def get_request(self):
        return self.registry.get(current_thread())

    def delete_request(self):
        self.registry.pop(current_thread(), None)

    @staticmethod
    def get_request_id(request):
        return getattr(request, 'request_id', None)


request_context = RequestContext()
