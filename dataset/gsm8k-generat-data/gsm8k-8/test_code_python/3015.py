def solution():
    # Calculate the total amount of money Sam has
    total_money = 19 * 10 + 6 * 25

    # Calculate the cost of the candy bars
    candy_bar_cost = 4 * 3 * 10

    # Calculate the cost of the lollipop
    lollipop_cost = 1 * 25

    # Calculate the total cost of the candy and lollipop
    total_cost = candy_bar_cost + lollipop_cost

    # Calculate the amount of money left after the purchases
    remaining_money = total_money - total_cost

    result = remaining_money
    return result

print(solution())