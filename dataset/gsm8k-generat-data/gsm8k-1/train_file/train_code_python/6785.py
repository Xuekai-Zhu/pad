def solution():
    """The world record for longest fingernails is 26 inches. Sandy, who just turned 12 this month, has a goal for tying the record. Her fingernails are 2 inches long. Her fingernails grow at a rate of one-tenth of an inch per month. How old will she be when she achieves the world record?"""
    current_length = 2
    growth_rate = 1/10
    distance_to_record = 26 - current_length
    months_to_record = distance_to_record / growth_rate
    years_to_record = months_to_record / 12
    age_at_record = 12 + years_to_record
    result = age_at_record
    return result

print(solution())