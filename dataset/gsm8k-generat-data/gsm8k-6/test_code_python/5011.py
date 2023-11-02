def solution():
    # Calculate the cost per mani/pedi after the 25% discount
    cost_per_mani_pedi = 40.0 * (1 - 0.25)  # 25% off the regular rate of $40.00

    # Calculate the total cost of 5 mani/pedis
    total_cost = cost_per_mani_pedi * 5  # Charlotte is treating herself, her daughter, and 3 granddaughters
    result = total_cost
    return result

print(solution())