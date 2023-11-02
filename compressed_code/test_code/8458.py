def solution():
    
    squat_weight = 700
    bench_weight = 400
    deadlift_weight = 800
    
    squat_weight = squat_weight * 0.7 
    
    deadlift_weight -= 200 
    
    total_weight = squat_weight + bench_weight + deadlift_weight
    result = total_weight
    
    return result

print(solution())