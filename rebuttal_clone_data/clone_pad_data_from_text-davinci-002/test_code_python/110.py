def solution():
     """Marvin and Tina were selling candy bars to help fund their class trip. The candy bars cost $2 each. Marvin sold 35 candy bars total. Tina sold three times the number of candy bars as Marvin. How much more money did Tina make for the class trip selling candy bars compared to Marvin?"""
     candy_bar_price = 2
     candy_bars_sold_marvin = 35
     candy_bars_sold_tina = candy_bars_sold_marvin * 3
     money_made_marvin = candy_bars_sold_marvin * candy_bar_price
     money_made_tina = candy_bars_sold_tina * candy_bar_price
     money_difference = money_made_tina - money_made_marvin
     result = money_difference
     return result

print(solution())