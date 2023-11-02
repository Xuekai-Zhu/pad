def solution():
    max_weight = 80  # The bookcase can hold a maximum of 80 pounds
    hardcover_books = 70 * 0.5  # 70 hardcover books weighing half a pound each
    textbooks = 30 * 2  # 30 textbooks weighing 2 pounds each
    knick_knacks = 3 * 6  # 3 knick-knacks weighing 6 pounds each

    # Calculate the total weight of the collection
    total_weight = hardcover_books + textbooks + knick_knacks

    # Calculate the weight over the maximum weight limit
    over_limit_weight = total_weight - max_weight
    result = over_limit_weight
    return result

print(solution())