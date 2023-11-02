def solution():
    members = 20  # There are 20 members in the group
    price_per_candy_bar = 0.50  # Each candy bar costs $0.50
    average_bars_sold = 8  # Each member sold an average of 8 candy bars

    # Calculate the total number of candy bars sold
    total_bars_sold = members * average_bars_sold

    # Calculate the total amount of money earned from candy bars sales
    total_money_earned = total_bars_sold * price_per_candy_bar
    result = total_money_earned
    return result

print(solution())