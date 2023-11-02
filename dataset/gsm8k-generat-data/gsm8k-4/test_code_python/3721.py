def solution():
    """Jessica is having a sweet tooth and bought 10 chocolate bars, 10 packs of gummy bears, and 20 bags of chocolate chips. Her total rang up to $150. If the cost of a pack of gummy bears is $2 and a bag of chocolate chips costs $5, how much does 1 chocolate bar cost?"""
    # Define the number of chocolate bars, packs of gummy bears, and bags of chocolate chips purchased
    chocolate_bars = 10
    gummy_bears = 10
    chocolate_chips = 20

    # Define the cost of a pack of gummy bears and a bag of chocolate chips
    gummy_bears_cost = 2
    chocolate_chips_cost = 5

    # Define the total cost of the purchase
    total_cost = 150

    # Calculate the cost of the gummy bears and chocolate chips
    gummy_bears_total = gummy_bears * gummy_bears_cost
    chocolate_chips_total = chocolate_chips * chocolate_chips_cost

    # Calculate the cost of the chocolate bars
    chocolate_bars_cost = total_cost - gummy_bears_total - chocolate_chips_total
    chocolate_bar_cost = chocolate_bars_cost / chocolate_bars

    # return the result
    result = chocolate_bar_cost
    return result

print(solution())