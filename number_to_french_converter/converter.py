from number_to_french_converter.constants import UNIT_LIST, TENS_LIST, SPECIAL_TENS_DICT


class FrenchNumberConverter:
    def convert(self, number: int) -> str:
        if number == 0:
            return "zéro"
        if 0 < number < 10:
            return self._convert_units(number)
        if 10 <= number < 100:
            return self._convert_tens(number)
        if 100 <= number < 1000:
            return self._convert_hundreds(number)
        if 1000 <= number < 1000000:
            return self._convert_thousands(number)
        else:
            return "Number too large"

    def _convert_units(self, number: int) -> str:
        return UNIT_LIST[number]

    def _convert_tens(self, number: int) -> str:
        tens, units = divmod(number, 10)
        if 11 <= number <= 16:
            return self._convert_special_tens(number)
        if 71 <= number <= 76:
            return f"soixante-{self._convert_special_tens(number - 60)}"
        if 91 <= number <= 96:
            return f"quatre-vingt-{self._convert_special_tens(number - 80)}"

        units_part = f"-{self._convert_units(units)}"
        if units == 0:
            units_part = ""
        if units == 1 and tens > 1:
            units_part = "-et-un"
        return f"{TENS_LIST[tens]}{units_part}"

    def _convert_hundreds(self, number: int) -> str:
        hundreds, tens = divmod(number, 100)
        hundreds_part = (
            "cent" if hundreds == 1 else f"{self._convert_units(hundreds)}-cents"
        )
        tens_part = f"-{self._convert_tens(tens)}" if tens else ""
        hundreds_part = hundreds_part.rstrip("s") if tens else hundreds_part
        return f"{hundreds_part}{tens_part}"

    def _convert_thousands(self, number: int) -> str:
        thousands, remainder = divmod(number, 1000)
        thousands_part = (
            "mille" if thousands == 1 else f"{self.convert(thousands)}-milles"
        )
        remainder_part = f"-{self.convert(remainder)}" if remainder else ""
        thousands_part = thousands_part.rstrip("s") if remainder else thousands_part
        return f"{thousands_part}{remainder_part}"

    def _convert_special_tens(self, number: int) -> str:
        return SPECIAL_TENS_DICT[number]
