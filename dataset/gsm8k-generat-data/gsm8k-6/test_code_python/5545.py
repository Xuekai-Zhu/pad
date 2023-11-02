def solution():
    # Calculate the cost of each planter pot based on the number and cost of plants
    cost_per_pot = (15.00 + 4*4.00 + 4*3.50)  # cost of one planter pot
    # Calculate the total cost of all four planter pots
    total_cost = cost_per_pot * 4
    result = total_cost
    return result

print(solution())