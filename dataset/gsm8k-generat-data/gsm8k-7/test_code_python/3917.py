def solution():
    hours_per_day = 24
    wait_customs = 20
    quarantine_days = 14

    # Calculate the total hours of wait time
    total_wait_hours = wait_customs + (quarantine_days * hours_per_day)
    result = total_wait_hours
    return result

print(solution())