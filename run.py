import argparse
import ast
from number_to_french_converter.main import convert_list

parser = argparse.ArgumentParser(description="Converts integers to French.")
parser.add_argument(
    "-n", "--number-list", type=str, required=True, help="A list of integers"
)
args = parser.parse_args()

number_list = ast.literal_eval(args.number_list)
converted_number_list = convert_list(number_list)
print(converted_number_list)
