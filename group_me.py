from typing import TypeVar, Callable, List, Dict
from collections import defaultdict


T = TypeVar('T')
R = TypeVar('R')


def group(f: Callable[[T], R], items: List[T]) -> Dict[R, List[T]]:
    """Groups items by their value given by the provided function in a dictionary."""
    res: Dict[R, List[T]] = defaultdict(list)

    for item in items:
        key: R = f(item)
        res[key].append(item)

    return dict(res)
