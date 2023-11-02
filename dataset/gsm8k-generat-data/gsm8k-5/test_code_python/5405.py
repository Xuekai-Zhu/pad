def solution():
    total_training_time = 5  # Socorro needs to train for a total of 5 hours
    time_per_problemset = (10 + 20) / 60  # Socorro spends 10 minutes on multiplication and 20 minutes on division

    # Calculate the number of problem sets Socorro can complete in her total training time
    num_problemsets = total_training_time / time_per_problemset

    # Calculate the number of days required to complete the training
    num_days = num_problemsets / 2  # Socorro completes 2 problem sets per day

    result = num_days
    return result

print(solution())