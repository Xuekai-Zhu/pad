def solution():
    
    worms_per_toad = 3
    time_per_worm = 15
    total_worms = (6*60)//time_per_worm  
    total_toads = total_worms // worms_per_toad
    result = total_toads
    return result

print(solution())