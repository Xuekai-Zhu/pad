def solution():
    
    first_level_spaces = 90
    second_level_spaces = first_level_spaces + 8
    third_level_spaces = second_level_spaces + 12
    fourth_level_spaces = third_level_spaces - 9
    total_spaces = first_level_spaces + second_level_spaces + third_level_spaces + fourth_level_spaces
    remaining_spaces = total_spaces - 100
    result = remaining_spaces
    return result

print(solution())