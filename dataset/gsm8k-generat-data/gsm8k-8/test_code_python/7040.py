def solution():
    # Calculate the number of fully trained dolphins
    fully_trained = 20 / 4

    # Calculate the number of remaining dolphins
    remaining = 20 - fully_trained

    # Calculate the number of dolphins in training
    in_training = 2 * remaining / 3

    # Calculate the number of dolphins to be trained next month
    next_month = remaining - in_training

    result = next_month
    return result

print(solution())