__version__ = 0.1

from validictory import (
    validate, SchemaValidator, ValidationError, SchemaError
)

from .decorator import with_schema

__all__ = [
    'validate', 'SchemaValidator', 'ValidationError', 'SchemaError',
    'with_schema'
]
