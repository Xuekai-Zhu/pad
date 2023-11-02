def solution():
    work_hours = 8
    appointments = 2 * 3
    stamping_hours = work_hours - appointments
    applications_per_hour = 50
    total_applications = stamping_hours * applications_per_hour
    return total_applications

print(solution())