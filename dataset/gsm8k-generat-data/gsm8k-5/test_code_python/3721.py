def solution():
    num_chocolate_bars = 10
    num_gummy_bears = 10
    num_chocolate_chips = 20
    total_cost = 150
    cost_per_gummy_bear = 2
    cost_per_chocolate_chip = 5

    # Calculate the total cost of the chocolate bars
    total_cost_bars = total_cost - (num_gummy_bears * cost_per_gummy_bear) - (num_chocolate_chips * cost_per_chocolate_chip)

    # Calculate the cost per chocolate bar
    cost_per_bar = total_cost_bars / num_chocolate_bars
    result = cost_per_bar
    return result

print(solution())