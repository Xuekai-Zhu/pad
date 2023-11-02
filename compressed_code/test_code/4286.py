def solution():
    
    cat_eats_per_hour = 0.25   
    initial_kibble = 3
    remaining_kibble = 1
    hours_away = ((initial_kibble - remaining_kibble) / cat_eats_per_hour)
    result = hours_away
    return result

print(solution())