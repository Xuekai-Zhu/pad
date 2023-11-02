def solution():
    """Elizabeth wants to buy the steak knives from a bridal registry as a wedding gift. The couple registered for 2 steak knife sets and each set contains 4 steak knives. If Elizabeth buys both sets and they cost $80.00 per set, how much does each single steak knife cost?"""
    # Define the number of sets and knives
    num_sets = 2
    knives_per_set = 4

    # Calculate the total cost of both sets of knives
    total_cost = num_sets * 80

    # Calculate the cost per knife
    cost_per_knife = total_cost / (num_sets * knives_per_set)

    # Return the result
    result = cost_per_knife
    return result

print(solution())