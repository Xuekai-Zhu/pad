def solution():
    """Francis' family has 2 ukuleles, 4 guitars, and a certain number of violins. Each ukulele has 4 strings. Each guitar has 6 strings. Each violin has 4 strings. If the total number of strings among the ukuleles, guitars, and violins is 40 strings, how many violins does Francis' family have?"""
    ukuleles = 2
    guitars = 4
    ukulele_strings = 4
    guitar_strings = 6
    violin_strings = 4
    total_strings = 40
    ukulele_total_strings = ukuleles * ukulele_strings
    guitar_total_strings = guitars * guitar_strings
    total_strings_so_far = ukulele_total_strings + guitar_total_strings
    violin_strings_left = total_strings - total_strings_so_far
    violins = violin_strings_left / violin_strings
    result = violins
    return result

print(solution())