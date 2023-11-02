def solution():
    sudoku_options = 9
    roman_numerals = 7
    if roman_numerals >= sudoku_options:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())