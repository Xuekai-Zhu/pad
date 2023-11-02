def solution():
    
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