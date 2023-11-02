def solution():
    """John has to restring 3 basses with 4 strings each, twice as many guitars which have 6 strings each, and 3 fewer 8 string guitars than the normal guitars.  How many strings does he need?"""
    # Define the number of strings per instrument
    BASS_STRINGS = 4
    GUITAR_STRINGS = 6
    EIGHT_STRING_GUITAR_STRINGS = 8

    # Define the number of instruments
    num_basses = 3
    num_guitars = 2 * num_basses
    num_eight_string_guitars = num_guitars - 3

    # Calculate the total number of strings needed
    total_strings = (num_basses * BASS_STRINGS) + (num_guitars * GUITAR_STRINGS) + (num_eight_string_guitars * EIGHT_STRING_GUITAR_STRINGS)

    # Display the total number of strings needed
    result = total_strings
    return result

print(solution())