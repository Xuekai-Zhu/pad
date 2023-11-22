def solution():
    
    # Define the initial amount of water
    initial_water = 24

    # Calculate the amount of water given to the girls
    girls_water = initial_water / 6

    # Calculate the amount of water given to the boy
    boy_water = 6

    # Calculate the total amount of water given away
    total_given = 2 * girls_water + boy_water

    # Calculate the amount of water left
    water_left = initial_water - total_given

    # return the result
    result = water_left
    return result

print(solution())