def solution():
    """Cory bought a patio table and 4 chairs for $135. The patio table cost $55. If each chair cost the same amount, how much did each chair cost?"""
    # Define the cost of the patio table
    PATIO_TABLE_COST = 55

    # Define the total cost of the patio table and chairs
    TOTAL_COST = 135

    # Calculate the total cost of the chairs
    chair_cost = (TOTAL_COST - PATIO_TABLE_COST) / 4

    # Display the cost of each chair
    result = chair_cost
    return result

print(solution())