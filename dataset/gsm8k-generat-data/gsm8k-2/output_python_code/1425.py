def solution():
    """A clerk can process 25 forms per hour. If 2400 forms must be processed in an 8-hour day, how many clerks must you hire for that day?"""
    forms_per_clerk_per_hour = 25
    total_forms = 2400
    work_hours = 8
    total_forms_processed = forms_per_clerk_per_hour * work_hours * clerks_needed
    clerks_needed = math.ceil(total_forms / total_forms_processed)
    result = clerks_needed
    return result

print(solution())