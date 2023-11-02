def solution():
    # Calculate the cost of the unlimited plan
    unlimited_cost = 12

    # Calculate the cost of the alternative plan
    text_cost = (60/30) * 1  # $1 per 30 texts
    call_cost = (60/20) * 3  # $3 per 20 minutes of calls
    alternative_cost = text_cost + call_cost

    # Calculate the difference in cost between the two plans
    cost_difference = unlimited_cost - alternative_cost
    result = cost_difference
    return result

print(solution())