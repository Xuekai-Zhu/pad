def solution():
    ukuleles = 2
    guitars = 4
    ukulele_strings = 4
    guitar_strings = 6
    violin_strings = 4
    total_strings = 40
    total_ukulele_strings = ukuleles * ukulele_strings
    total_guitar_strings = guitars * guitar_strings
    total_violin_strings = total_strings - (total_ukulele_strings + total_guitar_strings)
    violins = total_violin_strings / violin_strings
    result = violins
    return result

print(solution())