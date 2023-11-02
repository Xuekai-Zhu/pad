def solution():
    total_hours_per_week = 20  # Cathy and Chris were supposed to work 20 hours per week
    total_weeks = 2 * 4  # They were supposed to work for 2 months, which is 4 weeks per month
    total_hours = total_hours_per_week * total_weeks  # Total hours they were supposed to work

    # Chris was sick for one week and Cathy took her shifts, adding an extra 20 hours of work for Cathy
    extra_hours = total_hours_per_week

    # Calculate total hours worked by Cathy
    total_cathy_hours = total_hours + extra_hours

    result = total_cathy_hours
    return result

print(solution())