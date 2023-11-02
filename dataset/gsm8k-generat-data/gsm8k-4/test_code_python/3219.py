def solution():
    """Cory bought a patio table and 4 chairs for $135. The patio table cost $55. If each chair cost the same amount, how much did each chair cost?"""
    # Define the cost of the patio table and the total cost of the purchase
    table_cost = 55
    total_cost = 135

    # Calculate the total cost of the chairs
    chair_cost_total = total_cost - table_cost

    # Divide the total cost of the chairs by the number of chairs to get the cost per chair
    num_chairs = 4
    chair_cost_each = chair_cost_total / num_chairs

    # Round the result to 2 decimal places
    result = round(chair_cost_each, 2)
    return result

print(solution())