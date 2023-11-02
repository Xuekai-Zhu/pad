def solution():
    
    telescope_time = 2 * 60 
    setup_time = 0.5 * 60 
    snack_time = setup_time * 3
    comet_time = 20
    total_time = telescope_time + setup_time + snack_time + comet_time
    percent_time_watching_comet = (comet_time / total_time) * 100
    result = round(percent_time_watching_comet)
    return result

print(solution())