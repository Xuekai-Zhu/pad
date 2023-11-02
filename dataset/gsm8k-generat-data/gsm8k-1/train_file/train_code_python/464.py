def solution(): 
    """A man is returning home from work and trying to decide which route to take. His first route option includes 3 stoplights. This route will take him 10 minutes if all three lights are green, but each light that is red will add 3 minutes to the trip. The second route does not include any stoplights and takes 14 minutes. If the man chooses the first route, how much longer will his trip be if all 3 stoplights are red?""" 

    route_1_greens = 3 
    route_1_green_time = 10 
    extra_time_per_red = 3 
    route_2_time = 14 

    # If all stoplights are red on Route 1, calculate the total time it will take 
    route_1_total_time = route_1_green_time + (route_1_greens * extra_time_per_red) 

    # Calculate the difference in time between the two routes 
    time_difference = route_1_total_time - route_2_time 

    result = time_difference 

    return result

print(solution())