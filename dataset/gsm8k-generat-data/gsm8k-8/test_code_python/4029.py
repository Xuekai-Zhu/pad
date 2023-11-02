def solution():
    # Calculate the profit per pop
    profit_per_pop = 1.50 - 0.90

    # Calculate the cost of 100 pencils
    cost_of_pencils = 100 * 1.80

    # Calculate the number of pops needed to cover the cost of pencils
    number_of_pops = cost_of_pencils / profit_per_pop

    result = number_of_pops
    return result

print(solution())