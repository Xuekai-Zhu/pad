def solution():
    forms_per_hour = 25  # A clerk can process 25 forms per hour
    forms_per_day = 2400  # 2400 forms must be processed in an 8-hour day
    hours_per_day = 8  # The clerk works for 8 hours per day

    # Calculate the number of clerks required to process 2400 forms in 8 hours
    clerks_required = forms_per_day / (forms_per_hour * hours_per_day)
    result = int(clerks_required) if clerks_required.is_integer() else int(clerks_required) + 1
    # We want the result to be an integer and to round up if necessary, to ensure all forms are processed
    return result

print(solution())