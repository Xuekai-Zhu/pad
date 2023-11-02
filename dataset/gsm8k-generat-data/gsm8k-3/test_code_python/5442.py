def solution():
    """Francis' family has 2 ukuleles, 4 guitars, and a certain number of violins. Each ukulele has 4 strings. Each guitar has 6 strings. Each violin has 4 strings. If the total number of strings among the ukuleles, guitars, and violins is 40 strings, how many violins does Francis' family have?"""
    # Define the number of strings per instrument
    UKULELE_STRINGS = 4
    GUITAR_STRINGS = 6
    VIOLIN_STRINGS = 4

    # Define the number of each instrument Francis' family has
    ukuleles = 2
    guitars = 4

    # Calculate the total number of strings from the ukuleles and guitars
    total_strings = ukuleles * UKULELE_STRINGS + guitars * GUITAR_STRINGS

    # Calculate the number of violins
    violins = (40 - total_strings) / VIOLIN_STRINGS

    # Display the number of violins
    result = violins
    return result

print(solution())