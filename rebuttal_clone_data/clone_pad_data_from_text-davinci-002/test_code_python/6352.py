def solution():
    chairs = 18
    tables = 6
    stools = 4
    wood_per_hour = 5
    wood_from_chairs = chairs * 6
    wood_from_tables = tables * 9
    wood_from_stools = stools * 2
    total_wood = wood_from_chairs + wood_from_tables + wood_from_stools
    hours_of_ warmth = total_wood / wood_per_hour
    result = hours_of_warmth
    
    return result

print(solution())