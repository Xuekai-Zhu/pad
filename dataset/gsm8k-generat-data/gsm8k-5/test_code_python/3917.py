def solution():
    hours_in_day = 24
    customs_wait = 20
    quarantine_days = 14

    # Total number of hours Jack had to wait
    total_wait = (quarantine_days * hours_in_day) + customs_wait
    result = total_wait
    return result

print(solution())