def solution():
    """John buys dinner plates and silverware. The silverware cost $20. The dinner plates cost 50% as much as the silverware.
    How much did he pay for everything?"""
    # Define the cost of silverware
    silverware_cost = 20

    # Calculate the cost of dinner plates
    dinner_plate_cost = 0.5 * silverware_cost

    # Calculate the total cost of both items
    total_cost = dinner_plate_cost + silverware_cost

    result = total_cost
    return result

print(solution())