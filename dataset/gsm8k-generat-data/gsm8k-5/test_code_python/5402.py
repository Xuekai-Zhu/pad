def solution():
    # Calculate the time taken to fly from New York to Chicago
    time_nyc_to_chicago = 4

    # Calculate the time the plane spends at the Chicago port
    time_chicago_port = 1

    # Calculate the time taken to fly from Chicago to Miami
    time_chicago_to_miami = 3 * time_nyc_to_chicago

    # Calculate the total time taken to travel from New York to Miami
    total_time = time_nyc_to_chicago + time_chicago_port + time_chicago_to_miami
    result = total_time
    return result

print(solution())