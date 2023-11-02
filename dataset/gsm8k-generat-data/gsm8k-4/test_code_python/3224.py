def solution():
    """Stephen rides his bicycle to church. During the first third of his trip, he travels at a speed of 16 miles per hour. 
    During the second third of his trip, riding uphill, he travels a speed of 12 miles per hour. 
    During the last third of his trip, he rides downhill at a speed of 20 miles per hour. 
    If each third of his trip takes 15 minutes, what is the distance Stephen rides his bicycle to church, in miles?"""
    
    # Calculate the time Stephen spends on each third of his trip
    time_per_third = 15/60  # 15 minutes converted to hours

    # Define the speeds Stephen travels at during each third of his trip
    speed_1 = 16
    speed_2 = 12
    speed_3 = 20

    # Calculate the distance Stephen covers in each third of his trip
    distance_1 = speed_1 * time_per_third
    distance_2 = speed_2 * time_per_third
    distance_3 = speed_3 * time_per_third

    # Calculate the total distance Stephen rides to church
    total_distance = distance_1 + distance_2 + distance_3
    
    # Round the result to 2 decimal places 
    result = round(total_distance, 2)
    return result

print(solution())