def solution():
    """John ends up serving on jury duty.  Jury selection takes 2 days.  The trial itself lasts 4 times as long as jury selection  It is a complicated trial.  The number of hours spent in jury deliberation was the equivalent of 6 full days.  They spend 16 hours a day in deliberation.  How many days does John spend on jury duty?"""
    # Define the number of days for jury selection and the multiplier for the trial length
    jury_selection_days = 2
    trial_length_multiplier = 4

    # Calculate the trial length in days
    trial_days = jury_selection_days * trial_length_multiplier

    # Calculate the total number of days on jury duty
    total_days = jury_selection_days + trial_days + 6

    # Calculate the total number of days, rounded up to the nearest whole day
    result = round(total_days)

    return result

print(solution())