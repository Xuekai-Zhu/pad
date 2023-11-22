def solution():
    
    # Define the total distance Soledad needs to hike in a month
    total_distance = 9300

    # Define the distance covered per day
    distance_per_day = 2 * 125

    # Calculate the remaining distance Soledad needs to hike in a month
    remaining_distance = total_distance - distance_per_day

    # Calculate the additional distance Soledad needs to hike per day to complete her journey on time
    additional_distance_per_day = remaining_distance / 2

    # Display the additional distance Soledad needs to hike per day
    result = additional_distance_per_day
    return result

print(solution())