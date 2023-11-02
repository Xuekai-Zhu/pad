def solution():
    # Calculate the total amount earned before being fined
    total_earned = 8 * 9  # Bill sold 8 ounces for $9 per ounce

    # Calculate the amount left after being fined
    amount_left = total_earned - 50  # fined $50

    result = amount_left
    return result

print(solution())