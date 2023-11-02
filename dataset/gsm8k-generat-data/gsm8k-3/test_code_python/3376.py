def solution():
    """John used to go to the gym multiple times a weak but because of lockdowns he hasn't been able to go.  He used to lift 700 for squat, 400 for bench, and 800 for deadlift.  For squat he lost 30% of his lift.  He didn't lose any weight on bench because he was able to train that at home and he lost 200 pounds on deadlift.  What is his new total?"""
    # Define the initial lifting weights
    squat_weight = 700
    bench_weight = 400
    deadlift_weight = 800

    # Calculate the new weights after lockdown
    squat_weight = squat_weight * 0.7
    deadlift_weight = deadlift_weight - 200

    # Calculate the new total weight
    new_total = squat_weight + bench_weight + deadlift_weight

    # Display the new total weight
    result = new_total
    return result

print(solution())