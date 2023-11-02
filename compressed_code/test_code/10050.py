def solution():
    
    ukulele_strings = 2 * 4
    guitar_strings = 4 * 6
    total_strings = 40
    violin_strings = total_strings - ukulele_strings - guitar_strings
    violins = violin_strings / 4
    result = violins
    return result

print(solution())