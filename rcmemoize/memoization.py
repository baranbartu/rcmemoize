import hashlib
from rcmemoize.request import request_context


def request_cycle_memoize(ignore_inputs=False):
    # if ignore_inputs is True, then args,kwargs will not be used
    # to generate cache key
    def outer_wrapper(f):
        def inner_wrapper(*args, **kwargs):
            cache_key = generate_cache_key(f, ignore_inputs, args, kwargs)
            result = memoization_registry.get(cache_key)
            if not result:
                result = f(*args, **kwargs)
                memoization_registry.set(cache_key, result)
            return result

        return inner_wrapper

    return outer_wrapper


def generate_cache_key(f, ignore_inputs, args, kwargs):
    # list values are exceptional,lists will be sorted before
    # generating cache key to keep cache key consistence
    cache_key = '%s.%s' % (f.__module__, f.__name__)
    if not ignore_inputs:
        list_kwargs_values = (
            [sorted(v) for k, v in kwargs.items() if isinstance(v, list)])
        other_kwargs_values = (
            [v for k, v in kwargs.items() if not isinstance(v, list)])
        kwargs_cache_key = '%s_%s' % (
            str(list_kwargs_values), str(other_kwargs_values))
        list_args_values = (
            [sorted(v) for v in list(args) if isinstance(v, list)])
        other_args_values = (
            [v for v in list(args) if not isinstance(v, list)])
        args_cache_key = '%s_%s' % (
            str(list_args_values), str(other_args_values))
        cache_key_suffix = '%s_%s' % (kwargs_cache_key, args_cache_key)
        cache_key = '%s_%s' % (
            cache_key, hashlib.md5(cache_key_suffix).hexdigest())
    return cache_key


class MemoizationRegistry(object):
    def __init__(self):
        self.registry = {}

    @staticmethod
    def get_request_id():
        request = request_context.get_request()
        if request:
            return getattr(request, 'request_id', None)

    def create_bucket(self, request_id):
        self.registry[request_id] = {}

    def delete_bucket(self, request_id):
        if request_id in self.registry:
            self.registry.pop(request_id)

    def get(self, cache_key):
        return self.registry.get(self.get_request_id(), {}).get(cache_key)

    def set(self, cache_key, result):
        request_id = self.get_request_id()
        if request_id in self.registry:
            self.registry.get(request_id)[cache_key] = result


memoization_registry = MemoizationRegistry()
