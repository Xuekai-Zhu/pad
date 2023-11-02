def solution():
    legos = 500
    used_legos = legos / 2
    missing_legos = 5
    legos_in_box = legos - used_legos - missing_legos
    result = legos_in_box
    return result

print(solution())