def solution():
    current_sleep = 6  # Tom currently gets 6 hours of sleep per day
    increase = 1/3  # Tom plans to increase his sleep by 1/3

    # Calculate the new amount of sleep Tom will get
    new_sleep = current_sleep + (current_sleep * increase)

    result = new_sleep
    return result

print(solution())