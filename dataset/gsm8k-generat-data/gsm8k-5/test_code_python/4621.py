def solution():
    bass_strings = 3 * 4  # John needs 12 strings for the basses
    guitars = 2 * 3  # John has to restring twice as many guitars as basses
    guitar_strings = guitars * 6  # Each guitar has 6 strings
    eight_string_guitars = guitars - 3  # John has 3 fewer 8 string guitars than the normal guitars
    eight_string_guitar_strings = eight_string_guitars * 8  # Each 8 string guitar has 8 strings

    # Calculate the total number of strings needed
    total_strings = bass_strings + guitar_strings + eight_string_guitar_strings
    result = total_strings
    return result

print(solution())