def solution():
    
    # Define the distance of walking on the beach and the distance on the sidewalk
    distance_beach = 2
    distance_sidewalk = 1

    # Calculate the walking speed on the sidewalk
    walking_sidewalk_speed = walking_sidewalk * 2

    # Calculate the walking time on the sidewalk
    walking_sidewalk_time = distance_sidewalk * walking_sidewalk_speed / walking_sidewalk_speed

    # Calculate the total walking time
    total_walking_time = walking_beach + walking_sidewalk_time

    # Convert the walking time from minutes to hours
    walking_time_hours = total_walking_time / 60

    # Display the walking time in hours
    result = walking_time_hours
    return result

print(solution())