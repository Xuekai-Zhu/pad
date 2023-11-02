def solution():
    # Calculate the total cost of the candy bars
    candy_bars_cost = 4 * 3  # each candy bar costs 3 dimes

    # Calculate the total cost of the lollipop
    lollipop_cost = 1 * 25  # 1 quarter is equal to 25 cents

    # Calculate the total amount of money used
    total_money_used = candy_bars_cost + lollipop_cost

    # Calculate the total amount of money Sam has
    total_money = (19 * 10) + (6 * 25)  # 1 dime is equal to 10 cents, 1 quarter is equal to 25 cents

    # Calculate the amount of money Sam has left
    money_left = total_money - total_money_used
    result = money_left
    return result

print(solution())