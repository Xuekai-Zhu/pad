def solution():
    """Marvin and Tina were selling candy bars to help fund their class trip. The candy bars cost $2 each. Marvin sold 35 candy bars total. Tina sold three times the number of candy bars as Marvin. How much more money did Tina make for the class trip selling candy bars compared to Marvin?"""
    # Define the price of each candy bar
    candy_price = 2

    # Calculate the total number of candy bars sold by Marvin and Tina
    marvin_candy_bars = 35
    tina_candy_bars = marvin_candy_bars * 3

    # Calculate the total amount of money made by Marvin and Tina
    marvin_money = marvin_candy_bars * candy_price
    tina_money = tina_candy_bars * candy_price

    # Calculate the difference in the amount of money made by Marvin and Tina
    difference = tina_money - marvin_money

    # Return the result
    result = difference
    return result

print(solution())