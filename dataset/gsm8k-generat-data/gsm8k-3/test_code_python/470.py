def solution():
    """A lot of people have been sick at Gary's workplace, so he's been working a lot of extra shifts to fill in for people. As a result, he's earned some overtime (where every hour after 40 he earns 1.5 times his normal wage.) His paycheck (before taxes are taken out) came out to $696. If Gary normally earns $12 per hour, how many hours did he work that week?"""
    # Define the regular hourly rate and overtime pay multiplier
    REGULAR_RATE = 12
    OVERTIME_MULTIPLIER = 1.5

    # Define the number of hours worked
    total_pay = 696
    regular_hours = 40
    overtime_pay = total_pay - (regular_hours * REGULAR_RATE)
    overtime_hours = overtime_pay / (REGULAR_RATE * OVERTIME_MULTIPLIER)
    total_hours = regular_hours + overtime_hours

    # Display the total number of hours worked
    result = total_hours
    return result

print(solution())