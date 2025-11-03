from typing import TypeVar, Callable, List, Dict


T = TypeVar('T')
R = TypeVar('R')


def group(f: Callable[[T], R], items: List[T]) -> Dict[R, List[T]]:
    """Groups items by their value given by the provided function in a dictionary."""
    res: Dict[R, List[T]] = {}

    for item in items:
        key: R = f(item)
        if key not in res:
            res[key] = []
        res[key].append(item)

    return res
