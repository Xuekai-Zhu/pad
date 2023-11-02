def solution():
    third_character_lines = 2

    # Calculate the number of lines the second character has
    second_character_lines = 3 * third_character_lines + 6

    # Calculate the number of lines the first character has
    first_character_lines = second_character_lines + 8

    result = first_character_lines
    return result

print(solution())