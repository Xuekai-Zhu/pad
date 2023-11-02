def solution():
    number_of_basses = 3
    number_of_guitars = 2 * number_of_guitars
    number_of_8_string_guitars = number_of_guitars - 3
    strings_per_bass = 4
    strings_per_guitar = 6
    strings_per_8_string_guitar = 8
    total_strings = (number_of_basses * strings_per_bass) + (number_of_guitars * strings_per_guitar) + (number_of_8_string_guitars * strings_per_8_string_guitar)
    result = total_strings
    return result

print(solution())