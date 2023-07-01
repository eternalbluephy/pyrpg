from typing import Any

class ParamsNotNull:

    def __init__(self, *params) -> None:
        self.params = params

    def __call__(self, func) -> Any:
        def wrapper(*args, **kwds):
            print(func.__code__.co_varnames)
            for param in self.params:
                if param not in func.__code__.co_varnames and param not in kwds:
                    raise NameError(f'Param \'{param}\' does exists in function \'{func.__name__}\' or it is a default param.')
                if param in func.__code__.co_varnames and args[func.__code__.co_varnames.index(param)] is None:
                    raise ValueError(f'Param \'{param}\' can not be None when calling function \'{func.__name__}\'.')
                if param in kwds and kwds[param] is None:
                    raise ValueError(f'Param \'{param}\' can not be None when calling function \'{func.__name__}\'.')
            return func(*args, **kwds)
        return wrapper

