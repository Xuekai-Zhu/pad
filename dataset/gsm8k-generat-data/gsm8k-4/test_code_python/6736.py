def solution():
    """One of the clubs at Georgia's school was selling carnations for a fundraising event. A carnation costs $0.50. They also had a special where you could buy one dozen carnations for $4.00. If Georgia sent a dozen carnations to each of her 5 teachers and bought one carnation for each of her 14 friends, how much money would she spend?"""
    # Define the cost of one carnation
    cost_per_carnation = 0.5

    # Calculate the cost of buying one dozen carnations with the special
    cost_per_dozen = 4.0
    carnations_per_dozen = 12
    cost_per_carnation_special = cost_per_dozen / carnations_per_dozen

    # Calculate the total number of carnations needed
    total_carnations = (carnations_per_dozen * 5) + 14

    # Calculate the total cost of buying all the carnations
    total_cost = (carnations_per_dozen * 5 * cost_per_carnation_special) + (14 * cost_per_carnation)

    # Return the result
    result = total_cost
    return result

print(solution())