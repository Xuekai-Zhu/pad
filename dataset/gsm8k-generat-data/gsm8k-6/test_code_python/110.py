def solution():
    # Calculate the total number of candy bars sold by Marvin
    marvin_bars = 35

    # Calculate the total number of candy bars sold by Tina
    tina_bars = 3 * marvin_bars

    # Calculate the total amount of money raised by Marvin and Tina
    total_money = (marvin_bars + tina_bars) * 2

    # Calculate the difference in money raised by Tina and Marvin
    tina_money = tina_bars * 2
    marvin_money = marvin_bars * 2
    difference = tina_money - marvin_money

    result = difference
    return result

print(solution())