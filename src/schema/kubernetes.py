from src.schema import YAMLSchema


class LabelSchema(YAMLSchema):
    """
    Label schema.
    """

    app: str


class MetadataSchema(YAMLSchema):
    """
    Metadata schema.
    """

    name: str | None = None
    labels: LabelSchema | None = None


class SpecSelectorSchema(YAMLSchema):
    """
    Selector schema.
    """

    match_labels: LabelSchema


class ContainerPortSchema(YAMLSchema):
    """
    Container port schema.
    """

    container_port: int


class ContainerSchema(YAMLSchema):
    """
    Container schema.
    """

    name: str
    image: str
    ports: list[ContainerPortSchema] | None = None


class TemplateSpecSchema(YAMLSchema):
    """
    Template spec schema.
    """

    containers: list[ContainerSchema]


class SpecTemplateSchema(YAMLSchema):
    """
    Spec template schema.
    """

    metadata: MetadataSchema
    spec: TemplateSpecSchema


class SpecSchema(YAMLSchema):
    """
    Spec schema.
    """

    replicas: int
    selector: SpecSelectorSchema
    template: SpecTemplateSchema
