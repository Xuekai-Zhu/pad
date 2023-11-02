def solution():
    """A clerk can process 25 forms per hour. If 2400 forms must be processed in an 8-hour day, how many clerks must you hire for that day?"""
    # Define the number of forms that can be processed in one hour and the length of the work day
    FORMS_PER_HOUR = 25
    WORK_HOURS_PER_DAY = 8

    # Calculate the total number of forms that can be processed in one day
    forms_per_day = FORMS_PER_HOUR * WORK_HOURS_PER_DAY

    # Calculate the number of clerks needed to process all the forms in one day
    clerks_needed = int((2400 + forms_per_day - 1) / forms_per_day)

    # Display the number of clerks needed
    result = clerks_needed
    return result

print(solution())