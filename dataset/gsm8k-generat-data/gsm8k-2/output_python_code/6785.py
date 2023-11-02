def solution():
    """The world record for longest fingernails is 26 inches. Sandy, who just turned 12 this month, has a goal for tying the record. Her fingernails are 2 inches long. Her fingernails grow at a rate of one-tenth of an inch per month. How old will she be when she achieves the world record?"""
    starting_fingernail_length = 2
    world_record_length = 26
    growth_rate = 0.1
    months_needed = (world_record_length - starting_fingernail_length) / growth_rate
    years_needed = months_needed / 12
    age_when_achieved = round(years_needed) + 12
    result = age_when_achieved
    return result

print(solution())