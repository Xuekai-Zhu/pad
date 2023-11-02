def solution():
    """During a race transmitted on television, five advertisements were shown, lasting 3 minutes each. One minute of advertising costs $4000. What was the cost of transmitting these advertisements during the race?"""
    # Define the cost per minute of advertising
    COST_PER_MINUTE = 4000

    # Define the number of advertisements and the length in minutes
    num_ads = 5
    length = 3

    # Calculate the total length of the advertisements in minutes
    total_length = num_ads * length

    # Calculate the total cost of the advertisements
    total_cost = total_length * COST_PER_MINUTE

    # Display the total cost
    result = total_cost
    return result

print(solution())