def solution():
    """John ends up serving on jury duty. Jury selection takes 2 days. The trial itself lasts 4 times as long as jury selection It is a complicated trial. The number of hours spent in jury deliberation was the equivalent of 6 full days. They spend 16 hours a day in deliberation. How many days does John spend on jury duty?"""
    jury_selection_days = 2
    trial_days = jury_selection_days * 4
    deliberation_hours = 6 * 24
    deliberation_days = deliberation_hours / 16
    total_days = jury_selection_days + trial_days + deliberation_days
    result = total_days
    return result

print(solution())