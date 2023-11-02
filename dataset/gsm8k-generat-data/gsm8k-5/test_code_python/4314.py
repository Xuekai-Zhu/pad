def solution():
    total_laundry = 80  # Carla needs to dry-clean 80 pieces of laundry
    start_time = 8  # Carla starts work at 8 AM
    end_time = 12  # Carla needs to finish by noon
    work_hours = end_time - start_time  # Carla has 4 hours to finish the work

    # Calculate the number of pieces of laundry Carla needs to clean per hour
    laundry_per_hour = total_laundry / work_hours
    result = laundry_per_hour
    return result

print(solution())