def solution():
    
    tape_length = 250
    field_width = 20
    field_length = 60
    perimeter = 2 * (field_width + field_length)
    tape_used = perimeter
    tape_leftover = tape_length - tape_used
    result = tape_leftover
    return result

print(solution())