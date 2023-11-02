def solution():
    """Jerry is writing a script for a skit with three characters. The first character has eight more lines than the second character. The third character only has two lines. The second character has six more than three times the number of lines the third character has. How many lines does the first character in Jerry’s skit script have?"""
    third_character_lines = 2
    second_character_lines = 3 * third_character_lines + 6
    first_character_lines = second_character_lines + 8
    result = first_character_lines
    return result

print(solution())