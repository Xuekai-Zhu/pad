def solution():
    tall_cupboard_capacity = 20
    wide_cupboard_capacity = 2 * tall_cupboard_capacity
    narrow_cupboard_shelf_capacity = 15 / 3

    # Calculate the total number of glasses that can be displayed in the narrow cupboard
    narrow_cupboard_capacity = 2 * narrow_cupboard_shelf_capacity

    # Calculate the total number of glasses that can be displayed in all cupboards
    total_capacity = tall_cupboard_capacity + wide_cupboard_capacity + narrow_cupboard_capacity - narrow_cupboard_shelf_capacity

    # Subtract one from the total number of glasses to account for the broken shelf
    num_displayed_glasses = total_capacity - 1
    result = num_displayed_glasses
    return result

print(solution())