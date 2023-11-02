def solution():
    """John has to restring 3 basses with 4 strings each, twice as many guitars which have 6 strings each, and 3 fewer 8 string guitars than the normal guitars. How many strings does he need?"""
    # Define the number of strings for each instrument
    bass_strings = 4
    guitar_strings = 6
    eight_string_guitar_strings = 8

    # Calculate the total number of strings needed for the basses
    bass_strings_total = 3 * bass_strings

    # Calculate the total number of strings needed for the normal guitars
    normal_guitars = 2 * 3     # Twice as many as the basses
    normal_guitar_strings_total = normal_guitars * guitar_strings

    # Calculate the total number of strings needed for the 8 string guitars
    eight_string_guitars = normal_guitars - 3     # Three fewer than the normal guitars
    eight_string_guitar_strings_total = eight_string_guitars * eight_string_guitar_strings

    # Calculate the total number of strings needed
    total_strings = bass_strings_total + normal_guitar_strings_total + eight_string_guitar_strings_total

    # return the result
    result = total_strings
    return result

print(solution())