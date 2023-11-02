def solution():
    """A dental office gives away 2 toothbrushes to every patient who visits.  His 8 hour days are packed and each visit takes .5 hours.  How many toothbrushes does he give in a 5 day work week?"""
    # Define the number of hours the office is open each day
    HOURS_PER_DAY = 8

    # Define the number of toothbrushes given to each patient
    TOOTHBRUSHES_PER_PATIENT = 2

    # Define the time per patient
    TIME_PER_VISIT = 0.5

    # Calculate the number of patients per day 
    patients_per_day = HOURS_PER_DAY / TIME_PER_VISIT

    # Calculate the number of toothbrushes given per day
    toothbrushes_per_day = patients_per_day * TOOTHBRUSHES_PER_PATIENT

    # Calculate the number of toothbrushes given in a 5 day work week
    toothbrushes_per_week = toothbrushes_per_day * 5

    # Display the total number of toothbrushes given
    result = toothbrushes_per_week
    return result

print(solution())