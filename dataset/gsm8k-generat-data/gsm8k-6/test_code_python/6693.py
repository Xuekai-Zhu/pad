def solution():
    # Calculate the number of haircuts John gets in a year
    # He gets a haircut when his hair grows to 9 inches, then he cuts it to 6 inches
    # So he gets a haircut every 4.5 months (9 inches / 1.5 inches per month)
    haircuts_per_year = 12 / 4.5

    # Calculate the cost of each haircut, including the tip
    cost_per_haircut = 45 * 1.2  # 20% tip added

    # Calculate the total cost of haircuts in a year
    total_cost = haircuts_per_year * cost_per_haircut
    result = total_cost
    return result

print(solution())