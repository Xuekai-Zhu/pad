def solution():
    # Calculate the cost of the unlimited plan
    unlimited_cost = 12

    # Calculate the cost of the alternative plan based on texts and calls
    text_cost = (60/30) * 1
    call_cost = (60/20) * 3
    alternative_cost = text_cost + call_cost

    # Calculate the savings with the alternative plan
    savings = unlimited_cost - alternative_cost
    result = savings
    return result

print(solution())