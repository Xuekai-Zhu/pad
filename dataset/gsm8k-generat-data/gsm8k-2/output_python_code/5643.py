def solution():
    """Andrew has 2 3-hour appointments today. He spends the rest of his 8-hour workday stamping permit applications. If he can stamp 50 permit applications an hour, how many permits total does he stamp today?"""
    appointment_time = 2 * 3
    stamping_time = 8 - appointment_time
    permits_per_hour = 50
    total_permits = stamping_time * permits_per_hour
    result = total_permits
    return result

print(solution())