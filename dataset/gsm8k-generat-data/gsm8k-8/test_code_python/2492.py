def solution():
    total_items = 7 + 4

    # Calculate the total amount earned from selling shirts
    shirt_total = 4 * 5

    # Calculate the total amount earned from selling all items
    total_earned = 69

    # Calculate the total amount earned from selling dresses
    dress_total = total_earned - shirt_total

    # Calculate the price per dress
    price_per_dress = dress_total / 7

    result = price_per_dress
    return result

print(solution())