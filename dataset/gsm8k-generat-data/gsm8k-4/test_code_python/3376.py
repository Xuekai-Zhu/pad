def solution():
    """John used to go to the gym multiple times a weak but because of lockdowns he hasn't been able to go. He used to lift 700 for squat, 400 for bench, and 800 for deadlift. For squat he lost 30% of his lift. He didn't lose any weight on bench because he was able to train that at home and he lost 200 pounds on deadlift. What is his new total?"""
    # Define the original weights for each lift
    squat_original = 700
    bench_original = 400
    deadlift_original = 800

    # Calculate the amount of weight lost on the squat lift
    squat_weight_lost = squat_original * 0.3

    # Calculate the new weight on the squat lift
    squat_new = squat_original - squat_weight_lost

    # Calculate the new weight on the bench lift
    bench_new = bench_original

    # Calculate the amount of weight lost on the deadlift lift
    deadlift_weight_lost = 200

    # Calculate the new weight on the deadlift lift
    deadlift_new = deadlift_original - deadlift_weight_lost

    # Calculate the new total weight
    total_new = squat_new + bench_new + deadlift_new

    # return the result
    result = total_new
    return result

print(solution())