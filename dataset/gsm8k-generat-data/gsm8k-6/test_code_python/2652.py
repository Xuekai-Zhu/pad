def solution():
    # Calculate the total amount of money collected so far
    total_money_collected = (10 * 3) + (5 * 15)  # 3 families gave $10 each and 15 families gave $5 each

    # Calculate the amount of money remaining to reach the goal
    remaining_money = 150 - total_money_collected
    result = remaining_money
    return result

print(solution())