from typing import Callable, TypeVar, Union, Tuple
from python_maybe.infix import Infix

A = TypeVar('A')
B = TypeVar('B')
E = TypeVar('E')

Maybe = Union[Tuple['just', A], Tuple['nothing']]


def just(value=None):
    return "just", value


def nothing():
    return "nothing", None


def from_value(value) -> Maybe[B]:
    return just(value) if value is not None else nothing()


@Infix
def then(maybe: Maybe[A], func: Callable[[A], Maybe[B]]) -> Maybe[B]:
    if maybe[0] == "just":
        return _cast_to_maybe(func(maybe[1]))
    elif maybe[0] == "nothing":
        return maybe


@Infix
def catch_nothing(maybe: Maybe[A], func: Callable[[A], Maybe[B]]) -> Maybe[B]:
    if maybe[0] == "nothing":
        return _cast_to_maybe(func())
    elif maybe[0] == "just":
        return maybe


@Infix
def map(maybe: Maybe[A], mapper: Callable[[A], B]) -> Maybe[B]:
    if maybe[0] == "just":
        return just(mapper(maybe[1]))
    elif maybe[0] == "nothing":
        return maybe


@Infix
def value_or_default(maybe: Maybe[A], value: Callable[[A], B], default_value: B):
    return maybe | from_maybe | (dict(if_just=value, if_nothing=lambda: default_value))


@Infix
def from_maybe(maybe: Maybe[A], dict_args: dict) -> B:
    if_just: Callable = dict_args['if_just']
    if_nothing: Callable = dict_args['if_nothing']

    if maybe[0] == "just" and if_just is not None:
        return if_just(maybe[1])
    elif maybe[0] == "nothing" and if_nothing is not None:
        return if_nothing()
    else:
        raise Exception('Invalid Maybe: {}, {}'.format(maybe, dict_args))


def _cast_to_maybe(result):
    if isinstance(result, tuple) and len(result) == 2:
        maybe_type, value = result
        if maybe_type == "just" or maybe_type == "nothing":
            return result
    return "just", result
