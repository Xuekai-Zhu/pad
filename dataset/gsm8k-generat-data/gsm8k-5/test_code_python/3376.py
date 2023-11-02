def solution():
    squat = 700 * 0.7  # John lost 30% of his squat lift
    bench = 400  # John didn't lose any weight on bench
    deadlift = 800 - 200  # John lost 200 pounds on deadlift

    # Calculate John's new total lift
    new_total = squat + bench + deadlift
    result = new_total
    return result

print(solution())