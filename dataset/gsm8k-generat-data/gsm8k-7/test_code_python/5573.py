def solution():
    num_muffins_left = 7

    # Calculate the total number of muffins that Amy brought to school throughout the week
    num_muffins_week = 1 + 2 + 3 + 4 + 5

    # Calculate the total number of muffins that Amy originally baked
    num_muffins_baked = num_muffins_week + num_muffins_left
    result = num_muffins_baked
    return result

print(solution())