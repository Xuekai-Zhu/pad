def solution():
    # Define the variables
    candy_bar_cost = 2
    marvin_candy_bars = 35
    tina_candy_bars = 3 * marvin_candy_bars

    # Calculate the total amount of money Marvin made
    marvin_money = marvin_candy_bars * candy_bar_cost

    # Calculate the total amount of money Tina made
    tina_money = tina_candy_bars * candy_bar_cost

    # Calculate the difference in money made
    money_difference = tina_money - marvin_money
    result = money_difference
    return result

print(solution())