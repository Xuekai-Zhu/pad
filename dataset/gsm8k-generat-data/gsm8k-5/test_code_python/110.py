def solution():
    candy_bar_cost = 2  # Each candy bar costs $2
    marvin_bars_sold = 35  # Marvin sold 35 candy bars
    tina_bars_sold = 3 * marvin_bars_sold  # Tina sold three times as many candy bars as Marvin
    marvin_earnings = marvin_bars_sold * candy_bar_cost  # Calculate Marvin's earnings
    tina_earnings = tina_bars_sold * candy_bar_cost  # Calculate Tina's earnings
    difference = tina_earnings - marvin_earnings  # Calculate the difference in earnings
    result = difference
    return result

print(solution())