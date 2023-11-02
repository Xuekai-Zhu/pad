def solution():
    num_basses = 3
    bass_strings = 4

    num_guitars = num_basses * 2
    guitar_strings = 6

    num_8string_guitars = num_guitars - 3
    eight_string_guitar_strings = 8

    # Calculate the total number of strings needed for all basses
    bass_total_strings = num_basses * bass_strings

    # Calculate the total number of strings needed for all regular guitars
    guitar_total_strings = num_guitars * guitar_strings

    # Calculate the total number of strings needed for all 8-string guitars
    eight_string_guitar_total_strings = num_8string_guitars * eight_string_guitar_strings

    # Calculate the total number of strings needed for all instruments
    total_strings = bass_total_strings + guitar_total_strings + eight_string_guitar_total_strings
    result = total_strings
    return result

print(solution())