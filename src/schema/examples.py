from src.schema import YAMLSchema
from src.schema.kubernetes import MetadataSchema, SpecSchema
from src.schema.products import ProductSchema
from src.schema.servers import ServerSchema
from src.schema.users import UserSchema


class ExampleYAMLSchema(YAMLSchema):
    """
    Example YAML schema representing and validating example .yaml file.
    Check files/a_input.yaml for example data.
    """

    api_version: str
    kind: str
    metadata: MetadataSchema
    spec: SpecSchema
    users: list[UserSchema] | None = None
    products: list[ProductSchema] | None = None
    servers: list[ServerSchema] | None = None
