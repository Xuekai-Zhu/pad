def solution():
    # Calculate John's new lifts after the lockdown
    squat = 0.7 * 700  # John lost 30% of his squat lift
    bench = 400  # John was able to train his bench lift at home
    deadlift = 800 - 200  # John lost 200 pounds on his deadlift lift

    # Calculate John's new total lift
    total_lift = squat + bench + deadlift
    result = total_lift
    return result

print(solution())