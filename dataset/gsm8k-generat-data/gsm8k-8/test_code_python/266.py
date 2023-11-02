def solution():
    # Calculate the total time John spends weightlifting each week
    weightlifting_time_per_day = 1
    weightlifting_time_per_week = weightlifting_time_per_day * 3

    # Calculate the total time John spends warming up and doing cardio each week
    cardio_time_per_day = weightlifting_time_per_day / 3
    cardio_time_per_week = cardio_time_per_day * 3

    # Calculate the total time John spends at the gym each week
    total_time_per_week = weightlifting_time_per_week + cardio_time_per_week

    result = total_time_per_week
    return result

print(solution())