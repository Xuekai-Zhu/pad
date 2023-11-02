def solution():
    
    full_ladder_steps = 11
    smaller_ladder_steps = 6
    full_ladder_climbs = 10
    smaller_ladder_climbs = 7
    total_climbs = (full_ladder_steps * full_ladder_climbs) + (smaller_ladder_steps * smaller_ladder_climbs)
    result = total_climbs
    return result

print(solution())