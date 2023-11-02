cameras.    
def solution():
    number_of_models = 6
    number_of_bathing_suits = 2
    number_of_evening_wear = 3
    number_of_runs = number_of_bathing_suits + number_of_evening_wear
    time_per_run = 2
    total_time = number_of_models * number_of_runs * time_per_run
    result = total_time
    return result

print(solution())