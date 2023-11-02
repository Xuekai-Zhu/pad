def solution():
    # Calculate the number of clerks needed to process 2400 forms in 8 hours
    forms_per_day = 2400
    hours_per_day = 8
    forms_per_hour = forms_per_day / hours_per_day
    clerks_needed = forms_per_hour / 25
    result = clerks_needed
    return result

print(solution())