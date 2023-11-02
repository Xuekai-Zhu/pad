def solution():
    """John used to go to the gym multiple times a weak but because of lockdowns he hasn't been able to go. He used to lift 700 for squat, 400 for bench, and 800 for deadlift. For squat he lost 30% of his lift. He didn't lose any weight on bench because he was able to train that at home and he lost 200 pounds on deadlift. What is his new total?"""
    squat_lift = 700
    bench_lift = 400
    deadlift_lift = 800

    # Calculate the new squat lift
    squat_lift *= 0.7

    # Calculate the new deadlift lift
    deadlift_lift -= 200

    # Calculate the new total
    total_lift = squat_lift + bench_lift + deadlift_lift
    result = total_lift
    return result

print(solution())