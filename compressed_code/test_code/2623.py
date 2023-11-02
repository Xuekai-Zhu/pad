def solution():
    
    squat_lift = 700
    bench_lift = 400
    deadlift_lift = 800

    
    squat_lift *= 0.7

    
    deadlift_lift -= 200

    
    total_lift = squat_lift + bench_lift + deadlift_lift
    result = total_lift
    return result

print(solution())