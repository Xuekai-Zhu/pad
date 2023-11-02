def solution():
    old_squat_lift = 700
    old_bench_lift = 400
    old_deadlift = 800
    new_squat_lift = old_squat_lift * 0.7
    new_deadlift = old_deadlift - 200
    new_total = new_squat_lift + old_bench_lift + new_deadlift
    result = new_total
    
    return result

print(solution())