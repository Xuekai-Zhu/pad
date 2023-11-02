def solution():
    dimes = 19
    quarters = 6
    candy_bars = 4
    candy_bar_cost = 3
    lollipop_cost = 25

    # Calculate the total cost of the candy bars
    candy_bar_total_cost = candy_bars * candy_bar_cost * 10  # Multiply by 10 to convert to cents

    # Calculate the cost of the lollipop
    lollipop_total_cost = lollipop_cost * 10  # Multiply by 10 to convert to cents

    # Calculate the total amount of money spent
    total_spent = candy_bar_total_cost + lollipop_total_cost

    # Calculate the total amount of money Sam has
    total_money = (dimes * 10) + (quarters * 25)

    # Calculate how much money Sam has left
    money_left = total_money - total_spent

    result = money_left
    return result

print(solution())