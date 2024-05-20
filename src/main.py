from pathlib import Path
from src.schema.examples import ExampleYAMLSchema
from src.utils.helpers import read_yaml, write_json, populate_db, write_yaml


def main():
    """
    Main function to read a YAML file, convert it to JSON, validate the data, populate the database,
    and save the validated data back to a YAML file.

    The function follows these steps:
        1. Set the directory with input and output files.
        2. Check if the directory exists and is a directory.
        3. Set the path to the input YAML file.
        4. Check if the input file exists and is a file.
        5. Read the YAML file to a Python dictionary.
        6. Set the path to the output JSON file.
        7. Save the dictionary to the JSON file.
        8. Check if the output file exists and is a file.
        9. Validate the data and create a Pydantic schema object from the YAML file.
        10. Pass the Pydantic model to database repositories for consumption.
        11. Set the path to the output YAML file.
        12. Save the Pydantic schema object to the YAML file.
    """

    # Set directory with input and output files
    files_dir = Path(__file__).parent.joinpath("files")

    # Check if directory exists and is a directory
    assert files_dir.exists(), f"Directory {files_dir} does not exist."
    assert files_dir.is_dir(), f"Path {files_dir} is not a directory."

    # Set path to YAML file provided externally
    a_input_yaml: Path = files_dir / "a_input.yaml"

    # Check if file exists and is a file
    assert a_input_yaml.exists(), f"File {a_input_yaml} does not exist."
    assert a_input_yaml.is_file(), f"Path {a_input_yaml} is not a file."

    # Read YAML file to python dictionary
    yaml_data: dict = read_yaml(a_input_yaml)

    # Set path to JSON file that will be created after conversion
    b_output_json: Path = files_dir / "b_output.json"

    # Save dictionary to JSON file
    write_json(b_output_json, yaml_data)

    # Check if file exists and is a file
    assert b_output_json.exists(), f"File {b_output_json} does not exist."
    assert b_output_json.is_file(), f"Path {b_output_json} is not a file."

    # Validate data and create pydantic schema object from YAML file
    example_object = ExampleYAMLSchema(**yaml_data)

    # Pass pydantic model to database repositories for consumption.
    # At this point, all validations have been done and we can be sure that the data is correct.
    populate_db(example_object)

    # === ADDITIONAL: Save pydantic schema object back to YAML file ===

    # Set path to YAML file that will be created from schema
    c_output_yaml = files_dir / "c_output.yaml"

    # Save pydantic schema object to YAML file
    write_yaml(
        c_output_yaml,
        example_object.model_dump(exclude_none=True, by_alias=True, exclude_unset=True),
    )


if __name__ == "__main__":
    main()
