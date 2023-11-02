def solution():
    """During a race transmitted on television, five advertisements were shown, lasting 3 minutes each. One minute of advertising costs $4000. What was the cost of transmitting these advertisements during the race?"""
    # Define the duration of each advertisement and the cost per minute
    AD_DURATION = 3
    COST_PER_MINUTE = 4000

    # Calculate the total duration of the advertisements
    total_duration = AD_DURATION * 5

    # Calculate the total cost of transmitting the advertisements
    total_cost = total_duration * COST_PER_MINUTE

    # return the result
    result = total_cost
    return result

print(solution())