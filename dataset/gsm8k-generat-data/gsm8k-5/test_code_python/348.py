def solution():
    initial_duration = 10  # Brian can hold his breath underwater for 10 seconds initially
    duration_week1 = 2 * initial_duration  # After the first week, he doubles the time to 20 seconds
    duration_week2 = 2 * duration_week1  # After the second week, he doubles it again to 40 seconds
    duration_week3 = 1.5 * duration_week2  # After the final week, he increases it by 50% to 60 seconds

    # Calculate the final duration of Brian's breath hold
    final_duration = duration_week1 + duration_week2 + duration_week3
    result = final_duration
    return result

print(solution())