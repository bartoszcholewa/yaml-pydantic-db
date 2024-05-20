from enum import Enum

from src.schema import YAMLSchema


class ProductCategories(str, Enum):
    """
    Product categories enumeration for YAML schema.
    """

    ELECTRONICS = "electronics"
    GADGETS = "gadgets"
    BOOKS = "books"
    NON_FICTION = "non-fiction"
    CLOTHING = "clothing"
    ACCESSORIES = "accessories"


class ProductSchema(YAMLSchema):
    """
    Product schema.
    """

    id: int
    name: str
    description: str
    price: float
    categories: list[ProductCategories]
