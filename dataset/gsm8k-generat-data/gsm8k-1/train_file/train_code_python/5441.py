def solution():
    """Francis' family has 2 ukuleles, 4 guitars, and a certain number of violins. Each ukulele has 4 strings. Each guitar has 6 strings. Each violin has 4 strings. If the total number of strings among the ukuleles, guitars, and violins is 40 strings, how many violins does Francis' family have?"""
    ukulele_strings = 2 * 4
    guitar_strings = 4 * 6
    total_strings = 40
    violin_strings = total_strings - ukulele_strings - guitar_strings
    violins = violin_strings / 4
    result = violins
    return result

print(solution())