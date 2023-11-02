def solution(): 
     

    route_1_greens = 3 
    route_1_green_time = 10 
    extra_time_per_red = 3 
    route_2_time = 14 

    
    route_1_total_time = route_1_green_time + (route_1_greens * extra_time_per_red) 

    
    time_difference = route_1_total_time - route_2_time 

    result = time_difference 

    return result

print(solution())