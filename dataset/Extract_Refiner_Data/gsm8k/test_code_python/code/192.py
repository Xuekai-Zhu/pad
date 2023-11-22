def solution():
    
    # Define the total weight of carrots and the number of restaurants
    total_weight = 200
    num_restaurants = 40

    # Calculate the weight of carrots per restaurant
    weight_per_restaurant = 2

    # Calculate the total weight of carrots used by the restaurants
    total_used = num_restaurants * weight_per_restaurant

    # Calculate the weight of carrots that will not be used
    unused_weight = total_weight - total_used

    # Display the weight of carrots that will not be used
    result = unused_weight
    return result

print(solution())