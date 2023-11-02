def solution():
    time_at_practice = 2  # Kyle goes to practice for 2 hours
    shooting_time = 1  # Kyle spends half of the time shooting
    running_time = (time_at_practice - shooting_time) / 3  # Kyle runs for twice the time he lifts weights, so he spends 1/3 of his time lifting weights
    weightlifting_time = running_time * 2  # Kyle runs for twice the time he lifts weights

    # Convert the weightlifting time to minutes
    weightlifting_time_minutes = weightlifting_time * 60
    result = weightlifting_time_minutes
    return result

print(solution())