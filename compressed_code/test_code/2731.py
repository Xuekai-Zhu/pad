def solution():
    
    telescope_setup_time = 2
    backyard_setup_time = 0.5
    snack_setup_time = 3 * backyard_setup_time
    comet_watching_time = 20/60 
    total_time = telescope_setup_time + backyard_setup_time + snack_setup_time + comet_watching_time
    comet_percentage = (comet_watching_time/total_time) * 100
    result = round(comet_percentage)
    return result

print(solution())