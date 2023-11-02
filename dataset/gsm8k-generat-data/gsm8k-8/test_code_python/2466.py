def solution():
    start_legos = 380
    lost_legos = 57
    sister_legos = 24

    remaining_legos = start_legos - lost_legos - sister_legos
    result = remaining_legos
    return result

print(solution())