def solution():
    game_price = 60
    candy_price = 5
    hourly_rate = 8
    hours_worked = 9

    # Calculate the total earnings from babysitting
    total_earnings = hourly_rate * hours_worked

    # Calculate the total cost of the purchases
    total_cost = game_price + candy_price

    # Calculate the amount of money left over
    money_left = total_earnings - total_cost
    result = money_left
    return result

print(solution())