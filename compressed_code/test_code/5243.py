def solution():
    
    starting_fingernail_length = 2
    world_record_length = 26
    growth_rate = 0.1
    months_needed = (world_record_length - starting_fingernail_length) / growth_rate
    years_needed = months_needed / 12
    age_when_achieved = round(years_needed) + 12
    result = age_when_achieved
    return result

print(solution())