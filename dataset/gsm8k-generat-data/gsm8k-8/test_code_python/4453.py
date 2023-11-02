def solution():
    # Calculate the total weight of the hardcover books
    hardcover_weight = 70 * 0.5

    # Calculate the total weight of the textbooks
    textbook_weight = 30 * 2

    # Calculate the total weight of the knick-knacks
    knickknack_weight = 3 * 6

    # Calculate the total weight of all the items
    total_weight = hardcover_weight + textbook_weight + knickknack_weight

    # Calculate the weight over the bookcase's limit
    weight_over_limit = total_weight - 80

    result = weight_over_limit
    return result

print(solution())