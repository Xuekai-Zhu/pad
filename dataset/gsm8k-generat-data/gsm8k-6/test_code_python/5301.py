def solution():
    # Calculate the number of lines for each character
    third_character_lines = 2
    second_character_lines = 6 + 3 * third_character_lines # second character has six more than three times the number of lines the third character has
    first_character_lines = second_character_lines + 8 # first character has eight more lines than the second character
    result = first_character_lines
    return result

print(solution())