def solution():
    
    num_racquets = 12
    synthetic_gut_time = 15
    polyester_gut_time = 22
    hybrid_gut_time = 18
    total_time = (synthetic_gut_time * num_racquets) + ( polyester_gut_time * num_racquets) + (hybrid_gut_time * num_racquets)
    result = total_time
    return result

print(solution())