def solution():
    
    # Define the distance to the home and the speeds on land and water
    distance = 200
    land_speed = 20
    water_speed = 10

    # Calculate the time to travel on land and water
    land_time = distance / land_speed
    water_time = distance / water_speed

    # Calculate the total time to return home
    total_time = land_time + water_time

    # Display the total time
    result = total_time
    return result

print(solution())