def solution():
    
    acclimation_period = 1
    basics_period = 2
    research_period = basics_period * 1.75
    dissertation_period = acclimation_period / 2
    total_time = acclimation_period + basics_period + research_period + dissertation_period
    result = total_time
    return result

print(solution())