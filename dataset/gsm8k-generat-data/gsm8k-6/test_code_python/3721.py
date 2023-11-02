def solution():
    total_items = 10 + 10 + 20  # Jessica bought 10 chocolate bars, 10 packs of gummy bears, and 20 bags of chocolate chips
    total_cost = 150  # Jessica's total bill was $150
    gummy_bears_cost = 2  # Cost of a pack of gummy bears
    chocolate_chips_cost = 5  # Cost of a bag of chocolate chips

    # Calculate the total cost of chocolate bars
    chocolate_bars_cost = total_cost - ((10 * gummy_bears_cost) + (20 * chocolate_chips_cost))
    # Divide total cost of chocolate bars by the number of chocolate bars to get the cost of 1 chocolate bar
    cost_of_one_chocolate_bar = chocolate_bars_cost / 10
    result = cost_of_one_chocolate_bar
    return result

print(solution())