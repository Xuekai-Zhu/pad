def solution():
    time_to_ubert = 10
    time_to_airport = time_to_ubert * 5
    time_to_check_bag = 15
    time_through_security = time_to_check_bag * 3
    time_until_boarding = 20
    time_until_takeoff = time_until_boarding * 2

    # Calculate the total time in minutes
    total_time_in_minutes = (
        time_to_ubert
        + time_to_airport
        + time_to_check_bag
        + time_through_security
        + time_until_boarding
        + time_until_takeoff
    )

    # Convert minutes to hours
    total_time_in_hours = total_time_in_minutes / 60

    result = total_time_in_hours
    return result

print(solution())