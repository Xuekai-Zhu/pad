def solution():
    
    # Calculate the distance John travels in the first 2 hours
    distance_first_2_hours = 2 * 60

    # Calculate the distance John travels in the next half-hour
    distance_next_half_hours = 0.5 * 80

    # Calculate the total distance John travels in 4 hours
    total_distance = distance_first_2_hours + distance_next_half_hours

    # Display the total distance
    result = total_distance
    return result

print(solution())