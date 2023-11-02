def solution():
    # Calculate the cost of Becky's apples before discount
    becky_cost = 20 * 0.45

    # Calculate the cost of Kelly's apples before discount
    kelly_cost = 20 * 0.50

    # Calculate the cost of Becky's apples after discount
    becky_cost -= 1

    # Calculate the cost of Kelly's apples after discount
    kelly_cost -= 1

    # Calculate the difference in cost between Kelly and Becky
    cost_difference = kelly_cost - becky_cost
    result = cost_difference
    return result

print(solution())