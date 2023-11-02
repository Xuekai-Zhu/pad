def solution():
    # Define the times for each task in minutes
    wash_time = 10
    oil_time = 15
    tire_time = 30

    # Calculate total time spent on each task
    total_wash_time = 9 * wash_time
    total_oil_time = 6 * oil_time
    total_tire_time = 2 * tire_time

    # Calculate total time spent on all tasks in minutes
    total_time = total_wash_time + total_oil_time + total_tire_time

    # Convert total time to hours
    hours = total_time / 60

    result = hours
    return result

print(solution())