def solution():
    # Calculate the total amount spent by Penny
    socks_cost = 4 * 2  # 4 pairs of socks for $2 each
    hat_cost = 7
    total_spent = socks_cost + hat_cost

    # Calculate the amount of money left with Penny
    money_left = 20 - total_spent
    result = money_left
    return result

print(solution())