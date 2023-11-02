def solution():
    # Initialize starting amounts
    carol_money = 60
    mike_money = 90
    weeks = 0

    # Loop until they have the same amount of money
    while carol_money != mike_money:
        # Update money amounts and weeks
        carol_money += 9
        mike_money += 3
        weeks += 1

    result = weeks
    return result

print(solution())