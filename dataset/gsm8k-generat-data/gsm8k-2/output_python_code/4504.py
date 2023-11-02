def solution():
    """Unrest leads to 30 days of protest in 21 different cities. In each city, there are 10 arrests per day. The average person spends 4 days in jail before trial and then spends half of a 2-week sentence. How many combined weeks of jail time are there?"""
    protest_days = 30
    num_cities = 21
    arrests_per_day = 10
    pre_trial_days = 4
    sentence_weeks = 1
    total_jail_time = 0

    # Calculate total number of arrests
    total_arrests = protest_days * num_cities * arrests_per_day

    # Calculate total pre-trial jail time
    pre_trial_jail_time = total_arrests * pre_trial_days

    # Calculate total sentence jail time
    sentence_days = sentence_weeks * 7
    sentence_jail_time = (total_arrests * sentence_days) / 2

    # Calculate total jail time
    total_jail_time = (pre_trial_jail_time + sentence_jail_time) / 7

    result = total_jail_time
    return result

print(solution())