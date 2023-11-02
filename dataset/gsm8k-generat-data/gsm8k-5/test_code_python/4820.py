def solution():
    total_amount = 3  # Danny starts with 3 bottles of soda
    drink_amount = 0.9  # Danny drinks 90% of one bottle
    friend_amount = 0.7  # Danny gives 70% of two bottles to his friends

    # Calculate the amount of soda Danny has left
    remaining_amount = (1 - drink_amount) + (2 * (1 - friend_amount))

    # Convert the remaining amount to a percentage of one bottle
    percentage_remaining = remaining_amount * 100 / 3

    result = percentage_remaining
    return result

print(solution())