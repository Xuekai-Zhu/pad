def solution():
    # Define the cost of the sweater and the proportion of savings spent on makeup
    sweater_cost = 20
    makeup_proportion = 3/4

    # Calculate the total amount spent on makeup
    makeup_cost = sweater_cost / (1 - makeup_proportion) * makeup_proportion

    # Calculate the original savings
    original_savings = makeup_cost + sweater_cost
    result = original_savings
    return result

print(solution())