def solution():
    
    seaweed = 400
    fire_seaweed = 0.5 * seaweed
    edible_seaweed = 0.25 * (seaweed - fire_seaweed)
    livestock_seaweed = seaweed - fire_seaweed - edible_seaweed
    result = livestock_seaweed
    return result

print(solution())