def solution():
    """Elizabeth wants to buy the steak knives from a bridal registry as a wedding gift.  The couple registered for 2 steak knife sets and each set contains 4 steak knives.  If Elizabeth buys both sets and they cost $80.00 per set, how much does each single steak knife cost?"""
    # Define the number of sets and knives per set
    NUM_SETS = 2
    KNIVES_PER_SET = 4

    # Define the cost per set
    SET_COST = 80.00

    # Calculate the total cost
    total_cost = NUM_SETS * SET_COST

    # Calculate the cost per knife
    cost_per_knife = total_cost / (NUM_SETS * KNIVES_PER_SET)

    # Display the cost per knife
    result = cost_per_knife
    return result

print(solution())