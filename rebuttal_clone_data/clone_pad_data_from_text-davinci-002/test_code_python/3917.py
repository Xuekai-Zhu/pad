def solution():
    hours_in_customs = 20
    days_in_quarantine = 14
    hours_in_day = 24
    total_hours = hours_in_customs + (days_in_quarantine * hours_in_day)
    result = total_hours
    return result

print(solution())