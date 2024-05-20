from enum import Enum

from pydantic import EmailStr

from src.schema import YAMLSchema


class UserAddressSchema(YAMLSchema):
    """
    User address schema.
    """

    street: str
    city: str
    state: str
    zip: int


class ColorEnumSchema(str, Enum):
    """
    Color enumeration for user preferences.
    """

    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class UserPreferencesSchema(YAMLSchema):
    """
    User preferences schema.
    """

    color: ColorEnumSchema
    food: list[str]


class BankAccountType(str, Enum):
    """
    Bank account type enumeration.
    """

    CHECKING = "checking"
    SAVINGS = "savings"


class BankAccountSchema(YAMLSchema):
    """
    Bank account schema.
    """

    type: BankAccountType
    number: int
    balance: float
    interest_rate: float | None = None


class UserSchema(YAMLSchema):
    """
    User schema.
    """

    name: str
    age: int
    email: EmailStr
    address: UserAddressSchema
    preferences: UserPreferencesSchema
    accounts: list[BankAccountSchema]
