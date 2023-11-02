def solution():
    """A clerk can process 25 forms per hour. If 2400 forms must be processed in an 8-hour day, how many clerks must you hire for that day?"""
    forms_per_hour = 25
    hours_per_day = 8
    forms_per_day = forms_per_hour * hours_per_day
    forms_to_process = 2400
    clerks_needed = forms_to_process // forms_per_day
    if forms_to_process % forms_per_day > 0:
        clerks_needed += 1
    result = clerks_needed
    return result

print(solution())