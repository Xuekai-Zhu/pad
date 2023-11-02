def solution():
    num_ukuleles = 2
    num_guitars = 4
    ukulele_strings = 4
    guitar_strings = 6
    violin_strings = 4
    total_strings = 40

    # Calculate the total number of strings from the ukuleles and guitars
    ukulele_string_total = num_ukuleles * ukulele_strings
    guitar_string_total = num_guitars * guitar_strings
    combined_string_total = ukulele_string_total + guitar_string_total

    # Calculate the number of strings from the violins
    violin_string_total = total_strings - combined_string_total
    num_violins = violin_string_total / violin_strings
    result = num_violins
    return result

print(solution())