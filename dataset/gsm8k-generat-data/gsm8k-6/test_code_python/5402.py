def solution():
    # Calculate the total time taken to travel from New York to Miami
    fly_time_to_chicago = 4  # hours
    stay_time_in_chicago = 1  # hour
    fly_time_to_miami = fly_time_to_chicago * 3  # the time to fly to Miami is three times the time to fly to Chicago
    total_time = fly_time_to_chicago + stay_time_in_chicago + fly_time_to_miami
    result = total_time
    return result

print(solution())