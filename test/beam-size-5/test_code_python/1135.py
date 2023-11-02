def solution():
    
    # Define the cost of each pack of bagels
    PACK_COST = 10.00

    # Define the number of bagels in each pack
    BAGELS_PER_PACK = 9

    # Calculate the total cost before discount
    total_cost_before_discount = PACK_COST * BAGELS_PER_PACK

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount * 0.9

    # Calculate the cost per bagel after discount
    cost_per_bagel = total_cost_after_discount / 4

    # Display the cost per bagel
    result = cost_per_bagel
    return result

print(solution())