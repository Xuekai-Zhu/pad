def solution():
    num_legos = 500
    used_legos = num_legos / 2
    missing_legos = 5
    remaining_legos = num_legos - used_legos - missing_legos
    result = remaining_legos
    return result

print(solution())