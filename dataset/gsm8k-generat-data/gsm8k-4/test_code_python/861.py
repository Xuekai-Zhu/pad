def solution():
    """A dental office gives away 2 toothbrushes to every patient who visits.  His 8 hour days are packed and each visit takes .5 hours.  How many toothbrushes does he give in a 5 day work week?"""
    # Calculate the number of patients seen in a day
    patients_per_day = 8 / 0.5

    # Calculate the number of toothbrushes given away per day
    toothbrushes_per_day = patients_per_day * 2

    # Calculate the total number of toothbrushes given away in a 5 day work week
    toothbrushes_per_week = toothbrushes_per_day * 5

    # Return the result
    result = toothbrushes_per_week
    return result

print(solution())