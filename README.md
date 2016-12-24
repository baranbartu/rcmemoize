# rcmemoize (Django)
##### Cache anything in the current request cycle in memory for preventing duplicate method callers.
##### It works for Django only for now. But can be contributed to extend other Python Web Frameworks like Flask, Bottle, TurboGears etc.

# Installation

```bash
pip install rcmemoize
```

# Configuration

##### Add bottom of the of the MIDDLEWARE_CLASSES

```bash
rcmemoize.middleware.memoization_middleware.RequestCycleMemoizationMiddleware
```

# Usage
```bash
from rcmemoize.memoization import request_cycle_memoize

@request_cycle_memoize()
def your_method(*args,**kwargs):
...
```

# CONTRIBUTE
##### All contributions are very welcomed!

