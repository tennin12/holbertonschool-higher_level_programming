#!/usr/bin/python3
def roman_to_int(roman_string):
    if(type(roman_string) != str or roman_string is None):
        return (0)
    roman = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "DM": 900,
        "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400}
    v = 0
    c = 0
    l = len(roman_string)
    while c < l:
        if c + 1 < l and roman_string[c:c + 2] in roman:
            v += roman[roman_string[c:c + 2]]
            c += 2
        else:
            v += roman[roman_string[c]]
            c += 1
        return v