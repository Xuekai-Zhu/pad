def solution():
    """Every 4 weeks, Helen hand washes her silk pillowcases. It takes 30 minutes to hand wash all of them. In 1 year, how much time does Helen spend hand washing her pillowcases?"""
    weeks_per_year = 52
    wash_frequency = 4
    wash_time = 30
    total_time = (weeks_per_year / wash_frequency) * wash_time
    result = total_time
    return result

print(solution())