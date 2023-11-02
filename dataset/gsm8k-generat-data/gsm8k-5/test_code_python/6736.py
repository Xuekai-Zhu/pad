def solution():
    cost_per_carnation = 0.5  # A carnation costs $0.50
    cost_per_dozen = 4.0  # A dozen carnations cost $4.00

    # Calculate the total cost for sending a dozen carnations to each of Georgia's 5 teachers
    cost_for_teachers = 5 * cost_per_dozen

    # Calculate the total cost for buying one carnation for each of Georgia's 14 friends
    cost_for_friends = 14 * cost_per_carnation

    # Calculate the total amount of money Georgia will spend
    total_cost = cost_for_teachers + cost_for_friends
    result = total_cost
    
    return result

print(solution())