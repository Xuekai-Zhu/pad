def solution():
    
    field_w = 20
    field_l = 60
    perimeter = 2 * (field_l + field_w)
    tape_needed = perimeter
    tape_leftover = 250 - tape_needed
    result = tape_leftover
    return result

print(solution())