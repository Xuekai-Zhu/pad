def solution():
    """Marvin and Tina were selling candy bars to help fund their class trip.  The candy bars cost $2 each.  Marvin sold 35 candy bars total.  
    Tina sold three times the number of candy bars as Marvin.  How much more money did Tina make for the class trip selling candy bars compared to Marvin?"""
    
    # Define the variables
    candy_bar_cost = 2
    marvin_candy_bars = 35
    tina_candy_bars = 3 * marvin_candy_bars

    # Calculate the amount of money that Marvin made for the class trip
    marvin_money = marvin_candy_bars * candy_bar_cost

    # Calculate the amount of money that Tina made for the class trip
    tina_money = tina_candy_bars * candy_bar_cost

    # Calculate the difference in money made
    difference = tina_money - marvin_money

    result = difference
    return result

print(solution())