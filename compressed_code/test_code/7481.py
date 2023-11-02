def solution():
    
    seaweed_harvested = 400
    fire_seaweed = seaweed_harvested * 0.5
    remaining_seaweed = seaweed_harvested - fire_seaweed
    human_eatable_seaweed = remaining_seaweed * 0.25
    livestock_seaweed = remaining_seaweed - human_eatable_seaweed
    result = livestock_seaweed
    return result

print(solution())