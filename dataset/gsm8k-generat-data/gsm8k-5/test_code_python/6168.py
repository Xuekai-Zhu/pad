def solution():
    apples = 50  # 50 apples in the cafeteria
    oranges = 40  # 40 oranges in the cafeteria
    apple_price = 0.80  # $0.80 per apple
    orange_price = 0.50  # $0.50 per orange
    remaining_apples = 10  # 10 apples left
    remaining_oranges = 6  # 6 oranges left

    # Calculate the amount earned from selling the remaining apples and oranges
    total_earned = (remaining_apples * apple_price) + (remaining_oranges * orange_price)
    result = total_earned
    return result

print(solution())