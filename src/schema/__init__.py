from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class YAMLSchema(BaseModel):
    """Base schema for all pydantic models used for YAML serialization.

    Allows to keep camelCase in dictionary files and convert it to snake_case in Python objects.
    Additionally, converts enum objects to their values.

    """

    model_config = ConfigDict(
        alias_generator=to_camel,  # Convert any case to camelCase
        populate_by_name=True,  # Populate model from attributes
        from_attributes=True,  # Populate model from dictionary
        use_enum_values=True,  # Use enum values instead of objects
    )
