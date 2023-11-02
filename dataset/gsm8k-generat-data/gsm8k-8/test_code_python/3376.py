def solution():
    # Define the original lifts
    squat = 700
    bench = 400
    deadlift = 800

    # Calculate the decrease in squat lift
    squat_decrease = 0.3 * squat
    squat_new = squat - squat_decrease

    # Calculate the decrease in deadlift lift
    deadlift_decrease = 200
    deadlift_new = deadlift - deadlift_decrease

    # Calculate the new total lift
    total_new = squat_new + bench + deadlift_new
    result = total_new
    return result

print(solution())