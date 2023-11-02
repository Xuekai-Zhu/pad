def solution():
    """8 jumbo scallops weigh one pound and cost $24.00 a pound. Nate is pairing 2 scallops with a corn bisque as a light summer dinner. He’s cooking for 8 people. How much will the scallops cost?"""
    
    # Define the number of scallop pairs needed for the dinner
    scallop_pairs = 8

    # Define the weight of each scallop pair in pounds
    scallop_pair_weight = 1/4

    # Define the cost of one pound of scallops 
    scallop_price_per_pound = 24

    # Calculate the total weight of scallops needed
    total_scallop_weight = scallop_pairs * scallop_pair_weight
    
    # Calculate the total cost of the scallops
    total_scallop_cost = total_scallop_weight * scallop_price_per_pound
    
    # Return the result
    result = total_scallop_cost
    return result

print(solution())