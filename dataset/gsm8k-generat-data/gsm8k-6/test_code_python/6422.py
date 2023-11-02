def solution():
    # Calculate the total time it took Eric to reach the park
    time_to_reach_park = 20 + 10  # Eric runs for 20 minutes and then jogs for 10 minutes

    # Calculate the time it took Eric to return home
    time_to_return_home = time_to_reach_park * 3  # the return trip took 3 times as long as the trip there
    result = time_to_return_home
    return result

print(solution())