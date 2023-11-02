def solution():
    # Calculate the amount of time Kyle spends running
    running_time = (2 / 2) * (1 / 2) * 60 # he spends half the time shooting and half the time running and weight lifting
                                          # he runs for twice the time he spends weightlifting, so running time = 2 * weightlifting time
    weightlifting_time = (2 / 2) * (1 / 2) * 60 / 3 # total practice time is 2 hours = 120 minutes
                                                    # running time is twice the weightlifting time = 2 * weightlifting_time
                                                    # weightlifting_time + running_time = 120 mins, so weightlifting_time = (120 - 3 * running_time) / 3
    result = weightlifting_time
    return result

print(solution())