def solution():
    # Calculate the total amount made from selling shirts
    shirt_total = 4 * 5  # selling 4 shirts for $5 each

    # Calculate the amount made from selling dresses
    dress_total = 69 - shirt_total

    # Calculate the price of each dress
    price_per_dress = dress_total / 7  # selling 7 dresses

    result = price_per_dress
    return result

print(solution())