def solution():
    
    appointment_time = 2 * 3
    stamping_time = 8 - appointment_time
    permits_per_hour = 50
    total_permits = stamping_time * permits_per_hour
    result = total_permits
    return result

print(solution())