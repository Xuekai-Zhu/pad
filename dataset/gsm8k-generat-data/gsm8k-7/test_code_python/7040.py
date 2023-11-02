def solution():
    num_dolphins = 20

    # Calculate the number of fully trained dolphins
    num_fully_trained = num_dolphins // 4

    # Calculate the number of remaining dolphins
    num_remaining = num_dolphins - num_fully_trained

    # Calculate the number of dolphins currently in training
    num_in_training = (2/3) * num_remaining

    # Calculate the number of dolphins that will be trained next month
    num_next_month = num_remaining - num_in_training
    result = num_next_month
    return result

print(solution())