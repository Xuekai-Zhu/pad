def solution():
    """Carla needs to dry-clean 80 pieces of laundry by noon. If she starts work at 8 AM, how many pieces of laundry does she need to clean per hour?"""
    start_time = 8  # in AM
    end_time = 12  # in PM
    total_work_time = (end_time - start_time) * 60  # in minutes
    total_laundry = 80
    laundry_per_minute = total_laundry / total_work_time
    laundry_per_hour = laundry_per_minute * 60
    result = laundry_per_hour
    return result

print(solution())