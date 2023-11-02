def solution():
    # Calculate the total time John spends at the gym in a week
    weightlifting_time = 1  # John spends 1 hour lifting weights each gym day
    warmup_cardio_time = weightlifting_time / 3  # John spends a third of his weightlifting time on warmup/cardio
    total_time = (weightlifting_time + warmup_cardio_time) * 3  # John goes to the gym 3 times a week
    result = total_time
    return result

print(solution())