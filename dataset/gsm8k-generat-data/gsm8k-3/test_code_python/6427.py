def solution():
    """John ends up serving on jury duty.  Jury selection takes 2 days.  The trial itself lasts 4 times as long as jury selection  It is a complicated trial.  The number of hours spent in jury deliberation was the equivalent of 6 full days.  They spend 16 hours a day in deliberation.  How many days does John spend on jury duty?"""
    # Calculate the length of the trial in days
    trial_days = 4 * 2

    # Calculate the number of hours spent in jury deliberation
    deliberation_hours = 6 * 24

    # Calculate the number of days spent in deliberation
    deliberation_days = deliberation_hours / 16

    # Calculate the total number of days spent on jury duty
    total_days = 2 + trial_days + deliberation_days

    # Display the total number of days
    result = total_days
    return result

print(solution())