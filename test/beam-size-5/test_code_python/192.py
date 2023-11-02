def solution():
    
    # Define the total amount of carrots and the number of restaurants
    total_carrots = 200
    num_restaurants = 40

    # Define the amount of carrots each restaurant will receive
    carrots_per_restaurant = 2

    # Calculate the total amount of carrots used
    total_carrots_used = num_restaurants * carrots_per_restaurant

    # Calculate the amount of carrots not used
    carrots_not_used = total_carrots - total_carrots_used

    # return the result
    result = carrots_not_used
    return result

print(solution())