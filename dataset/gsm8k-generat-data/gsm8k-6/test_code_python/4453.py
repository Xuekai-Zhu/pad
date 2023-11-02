def solution():
    # Calculate the total weight of the items
    total_hardcover_weight = 70 * 0.5  # each hardcover book weighs 0.5 pounds
    total_textbook_weight = 30 * 2  # each textbook weighs 2 pounds
    total_knickknack_weight = 3 * 6  # each knick-knack weighs 6 pounds
    total_weight = total_hardcover_weight + total_textbook_weight + total_knickknack_weight

    # Calculate the weight over the bookcase's weight limit
    over_limit_weight = total_weight - 80
    result = over_limit_weight
    return result

print(solution())