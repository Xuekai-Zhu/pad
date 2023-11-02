def solution():
    route1_stoplights = 3
    route1_green_time = 10
    route1_red_time = 3

    route2_time = 14

    # Calculate the worst case scenario time for route 1 (all stoplights are red)
    route1_time = route1_green_time + (route1_stoplights * route1_red_time)

    # Calculate the difference in time between the two routes
    time_difference = route1_time - route2_time
    result = time_difference
    return result

print(solution())