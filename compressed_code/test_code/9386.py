def solution():
    
    sets_per_show = 5
    new_sets_per_show = 6
    shows_per_night = 1
    nights = 30
    total_sets_used = sets_per_show * shows_per_night * nights
    total_sets_given_away = new_sets_per_show * shows_per_night * nights
    total_sets = total_sets_used + total_sets_given_away
    result = total_sets
    
    return result

print(solution())