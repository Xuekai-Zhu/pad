def solution():
    # Define variables
    no_requirement = True
    arabic_numerals = True
    roman_numerals = False
    # Check if FDA requires sell by dates using Roman Numerals
    if no_requirement and arabic_numerals and not roman_numerals:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())