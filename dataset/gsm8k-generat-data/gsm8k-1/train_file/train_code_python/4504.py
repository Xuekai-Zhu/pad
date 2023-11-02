def solution():
    """Unrest leads to 30 days of protest in 21 different cities. In each city, there are 10 arrests per day. The average person spends 4 days in jail before trial and then spends half of a 2-week sentence. How many combined weeks of jail time are there?"""
    days_of_protest = 30
    num_cities = 21
    arrests_per_day = 10
    pre_trial_days = 4
    sentence_half_weeks = 1
    total_arrests = num_cities * days_of_protest * arrests_per_day
    total_jail_days = total_arrests * (pre_trial_days + sentence_half_weeks * 2 * 7)
    total_jail_weeks = total_jail_days / (7 * 2)
    result = total_jail_weeks
    return result

print(solution())