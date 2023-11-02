def solution():
    
    time_shopping = 2
    time_setting_up = 0.5
    time_making_snacks = time_setting_up * 3
    time_watching_comet = 0.3333
    total_time = time_shopping + time_setting_up + time_making_snacks + time_watching_comet
    percent_watching_comet = (time_watching_comet / total_time) * 100
    result = percent_watching_comet
    return result

print(solution())