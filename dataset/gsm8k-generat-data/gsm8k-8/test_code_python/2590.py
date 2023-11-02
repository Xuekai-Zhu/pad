def solution():
    # Calculate the total capacity of the wide cupboard
    wide_capacity = 2 * 20

    # Calculate the total capacity of the narrow cupboard
    narrow_capacity = 15 * 2  # 2 shelves, each can hold 15 glasses

    # One shelf in the narrow cupboard is broken, so its capacity is reduced by one-third
    broken_shelf_capacity = narrow_capacity / 3
    narrow_capacity -= broken_shelf_capacity

    # Calculate the total capacity of all the cupboards
    total_capacity = 20 + wide_capacity + narrow_capacity

    result = total_capacity
    return result

print(solution())