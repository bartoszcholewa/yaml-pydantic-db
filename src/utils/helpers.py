import json
from pathlib import Path

import yaml

from src.schema.examples import ExampleYAMLSchema


class IndentDumper(yaml.SafeDumper):
    """
    Custom YAML Dumper with increased indent in arrays.

    Before:
        ```
        foo:
        - bar
        - baz
        ```

    After:
        ```
        foo:
          - bar
          - baz
        ```
    """

    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)


def read_yaml(file_path: str | Path) -> dict:
    """Read YAML file and return data as dict.

    Args:
        file_path (str | Path): Path to YAML file.

    Returns:
        dict: Data from YAML file.

    """

    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    return data


def write_json(file_path: str | Path, data: dict) -> None:
    """Write dict to JSON file.

    Args:
        file_path (str | Path): Path to JSON file.
        data (dict): Data to write to JSON file.

    """
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=True)


def write_yaml(file_path: str | Path, data: dict) -> None:
    """Write dict to YAML file.

    Args:
        file_path (str | Path): Path to YAML file.
        data (dict): Data to write to YAML file.

    """
    with open(file_path, "w") as file:
        yaml.dump(
            data=data,
            stream=file,
            Dumper=IndentDumper,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )


def populate_db(obj: ExampleYAMLSchema) -> None:
    """
    Populate database with data from YAML file.
    Example endpoint between .yaml file, pydantic model and database repositories.

    Args:
        obj (ExampleYAMLSchema): Pydantic model object.

    """
    assert isinstance(
        obj, ExampleYAMLSchema
    ), f"Object {obj} is not an instance of ExampleYAMLSchema."
