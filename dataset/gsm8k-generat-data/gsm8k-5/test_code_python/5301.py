def solution():
    third_char_lines = 2  # The third character has two lines
    second_char_lines = 6 + 3 * third_char_lines  # The second character has six more than three times the third character's lines
    first_char_lines = second_char_lines + 8  # The first character has eight more lines than the second character
    result = first_char_lines
    return result

print(solution())