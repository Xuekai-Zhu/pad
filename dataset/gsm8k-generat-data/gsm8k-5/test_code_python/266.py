def solution():
    days_per_week = 3  # John goes to the gym 3 times per week
    weightlifting_time = 1  # John spends 1 hour lifting weights each day
    cardio_time = weightlifting_time / 3  # John spends a third of his weightlifting time on cardio

    # Calculate the total time John spends at the gym per week
    total_time = (weightlifting_time + cardio_time) * days_per_week

    result = total_time
    return result

print(solution())