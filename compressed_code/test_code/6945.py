def solution():
    
    hunting_frequency = 6
    deer_caught_each_time = 2
    weight_of_each_deer = 600
    season_length_in_months = 3
    total_hunts_in_season = hunting_frequency * season_length_in_months
    total_deer_caught_in_season = total_hunts_in_season * deer_caught_each_time
    total_weight_of_deer_caught_in_season = total_deer_caught_in_season * weight_of_each_deer
    weight_of_deer_kept = total_weight_of_deer_caught_in_season / 2
    result = weight_of_deer_kept
    return result

print(solution())