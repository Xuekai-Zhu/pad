def solution():
    # Define the number of lines for the third character
    third_character_lines = 2

    # Calculate the number of lines for the second character
    second_character_lines = 3 * third_character_lines + 6

    # Calculate the number of lines for the first character
    first_character_lines = second_character_lines + 8

    result = first_character_lines
    return result

print(solution())