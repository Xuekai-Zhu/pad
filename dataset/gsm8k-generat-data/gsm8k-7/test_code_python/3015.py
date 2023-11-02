def solution():
    num_dimes = 19
    num_quarters = 6

    candy_bar_price = 3  # in dimes
    num_candy_bars = 4

    lollipop_price = 25  # in cents

    # Calculate the total amount of money spent on candy bars
    candy_bar_cost = candy_bar_price * num_candy_bars

    # Calculate the total amount of money spent on the lollipop
    lollipop_cost = lollipop_price

    # Calculate the total amount of money spent
    total_spent = candy_bar_cost + lollipop_cost

    # Calculate the total amount of money in cents
    total_money = (num_dimes * 10) + (num_quarters * 25)

    # Calculate the remaining amount of money in cents after buying the candy bars and lollipop
    remaining_money = total_money - total_spent

    result = remaining_money
    return result

print(solution())