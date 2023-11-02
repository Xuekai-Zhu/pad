def solution():
    
    season_days = 213
    first_fisherman_rate = 3
    second_fisherman_rate_stage_1 = 1
    second_fisherman_rate_stage_2 = 2
    second_fisherman_rate_stage_3 = 4
    
    
    first_fisherman_fish_caught = first_fisherman_rate * season_days
    
    
    second_fisherman_fish_caught = 0
    for day in range(1, season_days+1):
        if day <= 30:
            second_fisherman_fish_caught += second_fisherman_rate_stage_1
        elif day <= 90:
            second_fisherman_fish_caught += second_fisherman_rate_stage_2
        else:
            second_fisherman_fish_caught += second_fisherman_rate_stage_3
    
    
    fish_difference = abs(first_fisherman_fish_caught - second_fisherman_fish_caught)
    
    result = fish_difference
    return result

print(solution())