def solution():
    time_per_house = 20 # in minutes
    time_available = 180 # in minutes (3 hours)

    # Calculate the number of houses that can be painted in the available time
    num_houses = time_available // time_per_house
    
    result = num_houses
    return result

print(solution())