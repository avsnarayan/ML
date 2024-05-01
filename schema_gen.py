import json

def get_schema(data, parent_key=''):
    """
    Recursively traverse the JSON data and extract its schema.
    """
    schema = {}
    if isinstance(data, dict):
        for key, value in data.items():
            if parent_key:
                new_key = parent_key + '.' + key
            else:
                new_key = key
            schema[new_key] = get_schema(value, new_key)
    elif isinstance(data, list):
        if data:  # If list is not empty
            schema[parent_key] = get_schema(data[0], parent_key)
        else:  # Empty list
            schema[parent_key] = 'Empty list'
    else:
        schema[parent_key] = type(data).__name__
    return schema

def main():
    # Path to your JSON file
    json_file_path = '/Users/narayan.ambatipudi/pretty.json'

    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            schema = get_schema(data)
            print(json.dumps(schema, indent=4))
    except FileNotFoundError:
        print(f"File '{json_file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file '{json_file_path}'.")

if __name__ == "__main__":
    main()
