def solution():
    
    third_character_lines = 2
    second_character_lines = 6 + (3 * third_character_lines)
    first_character_lines = second_character_lines + 8
    result = first_character_lines
    return result

print(solution())