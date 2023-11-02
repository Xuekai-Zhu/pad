def solution():
    # Define the number of ukuleles and guitars
    num_ukuleles = 2
    num_guitars = 4

    # Calculate the total number of strings from the ukuleles and guitars
    ukulele_strings = num_ukuleles * 4
    guitar_strings = num_guitars * 6
    total_strings = ukulele_strings + guitar_strings

    # Calculate the number of violin strings
    violin_strings = 40 - total_strings
    num_violins = violin_strings // 4

    result = num_violins
    return result

print(solution())