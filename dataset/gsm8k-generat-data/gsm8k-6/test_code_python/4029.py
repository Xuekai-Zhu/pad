def solution():
    # Calculate the profit per ice-pop
    profit_per_pop = 1.50 - 0.90  # selling price minus cost price

    # Calculate the total cost of buying 100 pencils
    total_pencil_cost = 100 * 1.80

    # Calculate the number of ice-pops needed to make the required amount of money
    pops_needed = total_pencil_cost / profit_per_pop
    result = int(pops_needed)  # round down to nearest integer
    return result

print(solution())