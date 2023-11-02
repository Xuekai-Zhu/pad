def solution():
    # Calculate the total time Tim spent watching the half-hour show
    half_hour_total_time = 0.5 * 24

    # Calculate the total time Tim spent watching the 1-hour show
    one_hour_total_time = 1 * 12

    # Calculate the total time Tim spent watching TV
    total_time = half_hour_total_time + one_hour_total_time

    # Convert the total time to hours
    total_time_in_hours = total_time / 2

    result = total_time_in_hours
    return result

print(solution())