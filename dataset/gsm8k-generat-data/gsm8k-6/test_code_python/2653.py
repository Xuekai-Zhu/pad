def solution():
    # Calculate the cost of the beef and oil
    cost_beef = 3 * 4  # 3 pounds of beef that cost $4 per pound
    cost_oil = 1  # a liter of oil that costs $1
    total_cost = 16  # total cost of the grocery

    # Calculate the cost of the chicken
    cost_chicken = total_cost - cost_beef - cost_oil

    # Calculate how much each person should pay for the chicken
    each_pay = cost_chicken / 3  # Mary and her two friends agreed to pay evenly
    result = each_pay
    return result

print(solution())