def solution():
    """Alexa and Emily open up a lemonade stand in the front yard. They spent $10 for lemons, $5 for sugar and $3 for cups. The lemonade is $4 a cup. They sell a total of 21 cups. How much profit did Alexa and Emily make after paying off expenses?"""
    lemon_cost = 10
    sugar_cost = 5
    cup_cost = 3
    total_cost = lemon_cost + sugar_cost + cup_cost
    cups_sold = 21
    price_per_cup = 4
    total_revenue = cups_sold * price_per_cup
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())