def solution():
    
    ribbon_length = 30
    num_parts = 6
    used_parts = 4
    remaining_parts = num_parts - used_parts
    unused_ribbon = remaining_parts * (ribbon_length / num_parts)
    result = unused_ribbon
    return result

print(solution())