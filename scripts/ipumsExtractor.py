import csv
import pandas as pd

def parse_string(string, variable_info):
  """
  Parses a string based on the provided variable information and returns a dictionary.

  Args:
    string: The string to parse.
    variable_info: A dictionary containing variable definitions with 'start' and 'end' keys.

  Returns:
    A dictionary containing the parsed data.
  """

  parsed_data = {}
  for name, info in variable_info.items():
    value = string[info["start"] - 1 : info["end"]]
    if info.get("type") == "int":  # Check for optional 'type' in the specification
        value = int(value)
    parsed_data[name] = value
  return parsed_data

variable_info = {
    "YEAR": {"type": "int", "start": 1, "end": 4},
    "SERIAL": {"type": "str", "start": 5, "end": 12},  # Serial numbers often serve as identifiers  
    "PERNUM": {"type": "str", "start": 25, "end": 28},
    "HHWT": {"type": "str", "start": 13, "end": 22}, 
    "PERWT": {"type": "str", "start": 29, "end": 38},  # Might potentially be int type
    "STATEFIP": {"type": "int", "start": 23, "end": 24}, 
    "RACE": {"type": "str", "start": 39, "end": 39},
    "RACED": {"type": "str", "start": 40, "end": 42},
    "OCC": {"type": "code", "start": 43, "end": 46, "codebook": "path/to/your/codebook.txt"} 
}

with open('./data/usa_00004.dat', 'r') as file, open('./data/output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write header row (column names)
    csv_writer.writerow(variable_info.keys())

    for line in file:
        parsed_data = parse_string(line, variable_info)
        csv_writer.writerow(parsed_data.values())
        print(parsed_data)
