def solution():
    """A lot of people have been sick at Gary's workplace, so he's been working a lot of extra shifts to fill in for people. As a result, he's earned some overtime (where every hour after 40 he earns 1.5 times his normal wage.) His paycheck (before taxes are taken out) came out to $696. If Gary normally earns $12 per hour, how many hours did he work that week?"""
    normal_wage = 12
    overtime_wage = normal_wage * 1.5
    total_earnings = 696
    regular_hours = 40
    overtime_hours = (total_earnings - (normal_wage * regular_hours)) / overtime_wage
    total_hours = regular_hours + overtime_hours
    result = total_hours
    return result

print(solution())