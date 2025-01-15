import functools
import threading

class Cache:
    def __init__(self, depth):
        self.depth = depth
        self.cache = {}
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            return self.cache.get(key)

    def set(self, key, value):
        with self.lock:
            if len(self.cache) >= self.depth:
                self.cache.pop(next(iter(self.cache)))
            self.cache[key] = value

def memorize(depth=1000):
    def decorator(fn):
        cache = Cache(depth)

        @functools.wraps(fn)
        def wrapper(*args):
            key = (fn.__name__,) + args
            
            cachedResult = cache.get(key)
            if cachedResult is not None:
                return cachedResult

            result = fn(*args)
            cache.set(key, result)
            return result

        return wrapper
    return decorator
