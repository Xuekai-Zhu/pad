def solution():
    days_per_week = 3
    hours_per_day = 1

    # Calculate the total time spent weightlifting each week
    total_weightlifting_time = days_per_week * hours_per_day

    # Calculate the time spent warming up and doing cardio each day
    cardio_time_per_day = hours_per_day / 3

    # Calculate the total time spent on warming up and cardio each week
    total_cardio_time = days_per_week * cardio_time_per_day

    # Calculate the total time spent at the gym each week
    total_time = total_weightlifting_time + total_cardio_time
    result = total_time
    return result

print(solution())