def solution():
    hours_in_workday = 8  # Andrew has 8 hours in his workday
    hours_in_appointments = 2 * 3  # Andrew has 2 appointments, each lasting 3 hours
    hours_stamp_permits = hours_in_workday - hours_in_appointments  # Andrew spends the remaining time stamping permit applications

    # Calculate the total number of permits Andrew will stamp
    permits_stamped = hours_stamp_permits * 50  # Andrew can stamp 50 permits per hour

    result = permits_stamped
    return result

print(solution())