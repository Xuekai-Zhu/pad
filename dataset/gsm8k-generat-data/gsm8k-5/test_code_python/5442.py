def solution():
    ukuleles = 2
    guitars = 4
    total_strings_ukuleles = ukuleles * 4
    total_strings_guitars = guitars * 6

    # Calculate the total number of strings used by the violins
    total_strings_violins = 40 - total_strings_ukuleles - total_strings_guitars

    # Calculate the number of violins
    violins = total_strings_violins / 4
    result = violins
    return result

print(solution())