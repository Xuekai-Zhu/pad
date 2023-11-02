def solution():
    # Define the total cost and the number of each item
    total_cost = 150
    num_chocolate_bars = 10
    num_gummy_bears = 10
    num_chocolate_chips = 20
    cost_gummy_bears = 2
    cost_chocolate_chips = 5

    # Calculate the total cost of the chocolate bars
    total_cost_chocolate_bars = total_cost - (num_gummy_bears * cost_gummy_bears) - (num_chocolate_chips * cost_chocolate_chips)
    # Calculate the cost of one chocolate bar
    cost_per_chocolate_bar = total_cost_chocolate_bars / num_chocolate_bars
    result = cost_per_chocolate_bar
    return result

print(solution())