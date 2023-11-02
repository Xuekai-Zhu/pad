def solution():
    
    num_models = 6
    sets_of_bathing_suits = 2
    sets_of_evening_wear = 3
    runway_trip_time = 2
    total_runs_per_model = sets_of_bathing_suits + sets_of_evening_wear
    total_runs = total_runs_per_model * num_models
    total_runway_time = total_runs * runway_trip_time
    result = total_runway_time
    return result

print(solution())