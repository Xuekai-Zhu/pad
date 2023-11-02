def solution():
    total_seaweed = 400
    seaweed_for_fire = total_seaweed * 0.5
    available_seaweed = total_seaweed - seaweed_for_fire
    seaweed_for_human = available_seaweed * 0.25
    seaweed_for_livestock = available_seaweed - seaweed_for_human
    result = seaweed_for_livestock
    
    return result

print(solution())