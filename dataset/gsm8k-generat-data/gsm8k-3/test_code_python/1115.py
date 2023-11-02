def solution():
    """8 jumbo scallops weigh one pound and cost $24.00 a pound.  Nate is pairing 2 scallops with a corn bisque as a light summer dinner.  He’s cooking for 8 people.  How much will the scallops cost?"""
    # Define the weight and cost per pound of the scallops
    WEIGHT_PER_POUND = 8
    COST_PER_POUND = 24.0

    # Calculate the cost of 2 scallops based on weight and cost per pound
    cost_per_two_scallops = COST_PER_POUND / WEIGHT_PER_POUND * 2

    # Calculate the total cost of scallops for 8 people
    total_cost_scallops = cost_per_two_scallops * 8

    # Display the total cost of scallops
    result = total_cost_scallops
    return result

print(solution())