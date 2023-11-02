def solution():
    """After Martha went grocery shopping she had 4 bottles of juice in the refrigerator and 4 bottles in the pantry. During the week Martha bought 5 more bottles of juice. If Martha and her family drank 3 bottles of juice during the week, how many bottles are left?"""
    initial_juice = 8
    new_juice = 5
    drank_juice = 3
    remaining_juice = initial_juice + new_juice - drank_juice
    result = remaining_juice
    return result

print(solution())