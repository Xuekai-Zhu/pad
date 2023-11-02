def solution():
    num_laundry = 80
    start_time = 8
    end_time = 12

    # Calculate the total number of hours to finish the job
    total_hours = end_time - start_time

    # Calculate the number of pieces of laundry to clean per hour
    laundry_per_hour = num_laundry / total_hours
    result = laundry_per_hour
    return result

print(solution())