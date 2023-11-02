def solution():
    swimming_time = 3 * 60  # Tobias spent 3 hours in the pool, converted to minutes
    swimming_speed = 100  # Tobias's swimming speed is 100 meters per 5 minutes
    pause_duration = 5  # Tobias takes a 5-minute pause after every 25 minutes of swimming

    swimming_distance = 0  # Initialize the swimming distance
    total_pause_time = 0  # Initialize the total pause time

    # Calculate the swimming distance and the total pause time
    for i in range(swimming_time):
        if i % 25 == 0 and i > 0:
            total_pause_time += pause_duration
        elif i % 5 == 0:
            swimming_distance += swimming_speed

    total_swimming_time = swimming_time - total_pause_time  # Subtract the pause time from the total swimming time

    # Calculate the total swimming distance
    total_swimming_distance = (total_swimming_time / 5) * swimming_speed

    # Add the remaining swimming distance after the last pause
    final_swimming_distance = swimming_distance + (total_swimming_distance % swimming_speed)

    result = final_swimming_distance
    return result

print(solution())