from typing import List
from number_to_french_converter.converter import FrenchNumberConverter


def convert_list(number_list: List[int]) -> List[str]:
    converter = FrenchNumberConverter()
    converted_number_list = [converter.convert(number) for number in number_list]
    return converted_number_list
