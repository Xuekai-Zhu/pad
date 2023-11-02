def solution():
    """Francis' family has 2 ukuleles, 4 guitars, and a certain number of violins. Each ukulele has 4 strings. Each guitar has 6 strings. Each violin has 4 strings. If the total number of strings among the ukuleles, guitars, and violins is 40 strings, how many violins does Francis' family have?"""
    # Define the number of ukuleles, guitars and total strings
    num_ukuleles = 2
    num_guitars = 4
    total_strings = 40

    # Calculate the total number of strings from ukuleles and guitars
    ukulele_strings = 4 * num_ukuleles
    guitar_strings = 6 * num_guitars
    total_ukulele_guitar_strings = ukulele_strings + guitar_strings

    # Calculate the number of strings from violins
    violin_strings = total_strings - total_ukulele_guitar_strings

    # Calculate the number of violins
    num_violins = violin_strings / 4

    # Return the result
    result = num_violins
    return result

print(solution())