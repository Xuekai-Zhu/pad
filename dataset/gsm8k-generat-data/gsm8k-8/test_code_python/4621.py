def solution():
    # Calculate the number of strings needed for the basses
    bass_strings = 3 * 4

    # Calculate the number of guitars and strings needed for them
    guitars = 2 * 3
    guitar_strings = guitars * 6

    # Calculate the number of 8-string guitars and strings needed for them
    eight_string_guitars = guitars - 3
    eight_string_strings = eight_string_guitars * 8

    # Calculate the total number of strings needed
    total_strings = bass_strings + guitar_strings + eight_string_strings
    result = total_strings
    return result

print(solution())