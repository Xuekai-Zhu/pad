def solution():
    
    # Define the weight of each bag of onions and the cost per pound of onions
    BAG_WEIGHT = 50
    ONION_COST = 1.5

    # Define the number of bags of onions purchased
    num_bags = 4

    # Calculate the total weight of the onions purchased
    total_weight = num_bags * BAG_WEIGHT

    # Calculate the total cost of the onions purchased
    total_cost = total_weight * ONION_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())