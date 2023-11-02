def solution():
    """After Martha went grocery shopping she had 4 bottles of juice in the refrigerator and 4 bottles in the pantry. During the week Martha bought 5 more bottles of juice. If Martha and her family drank 3 bottles of juice during the week, how many bottles are left?"""
    initial_juice = 8
    bought_juice = 5
    consumed_juice = 3
    remaining_juice = initial_juice + bought_juice - consumed_juice
    result = remaining_juice
    return result

print(solution())