def solution():
    word = "Mix"
    roman_numeral = "MIX"
    if word.isalpha() and roman_numeral.isalnum():
        result = "Yes"
    else:
        result = "No"
    return result

print(solution())