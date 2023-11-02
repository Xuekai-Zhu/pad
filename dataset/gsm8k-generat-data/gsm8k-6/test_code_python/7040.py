def solution():
    # Calculate the number of fully trained dolphins
    fully_trained = 20//4

    # Calculate the number of dolphins not fully trained
    remaining_dolphins = 20 - fully_trained

    # Calculate the number of dolphins currently in training
    currently_training = (2/3) * remaining_dolphins

    # Calculate the number of dolphins to be trained next month
    next_month = remaining_dolphins - currently_training

    result = next_month
    return result

print(solution())