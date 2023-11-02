def solution():
    # Calculate the time it takes for him to walk 3 miles with the backpack
    walk_time = 3 / 3  # walking at a speed of 3 miles per hour

    # Calculate the time it takes for him to run 10 miles
    run_time = 10 / 5  # running at a speed of 5 miles per hour

    # Calculate the total time he exercises each day
    exercise_time = walk_time + run_time

    # Calculate the total time he exercises each week
    weekly_exercise_time = exercise_time * 7

    result = weekly_exercise_time
    return result

print(solution())