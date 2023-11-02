def solution():
    starting_money = 20
    candy_bars = 4
    candy_bar_price = 2

    # Calculate the total cost of all candy bars
    total_cost = candy_bars * candy_bar_price

    # Calculate how much money Todd has left
    money_left = starting_money - total_cost
    result = money_left
    return result

print(solution())