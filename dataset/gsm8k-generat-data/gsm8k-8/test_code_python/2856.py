def solution():
    # Define the times for each step
    time_to_uber = 10
    time_to_airport = 5 * time_to_uber
    time_to_check_bag = 15
    time_to_security = 3 * time_to_check_bag
    time_to_board = 20
    time_to_takeoff = 2 * time_to_board

    # Calculate the total time in minutes
    total_time_in_minutes = (time_to_uber + time_to_airport + time_to_check_bag +
                             time_to_security + time_to_board + time_to_takeoff)

    # Convert to hours
    total_time_in_hours = total_time_in_minutes / 60

    result = total_time_in_hours
    return result

print(solution())