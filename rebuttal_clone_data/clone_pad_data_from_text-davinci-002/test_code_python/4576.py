def solution():
    drumsticks_per_show = 5
    sets_tossed = 6
    nights_played = 30
    total_sets = (drumsticks_per_show * nights_played) + (sets_tossed * nights_played)
    result = total_sets
    return result

print(solution())