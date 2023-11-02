def solution():
    # Calculate the total number of strings from ukuleles and guitars
    total_strings_ukuleles = 2 * 4  # Each ukulele has 4 strings
    total_strings_guitars = 4 * 6  # Each guitar has 6 strings
    total_strings = total_strings_ukuleles + total_strings_guitars  # Total number of strings from ukuleles and guitars
    # Calculate the number of violins Francis' family has
    num_violins = (40 - total_strings) / 4  # Each violin has 4 strings and total number of strings is 40
    result = num_violins
    return result

print(solution())