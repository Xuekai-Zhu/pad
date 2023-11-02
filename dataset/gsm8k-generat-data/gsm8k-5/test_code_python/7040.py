def solution():
    total_dolphins = 20  # There are 20 dolphins in the aqua park
    fully_trained_dolphins = total_dolphins // 4  # One-fourth of the dolphins are fully trained
    remaining_dolphins = total_dolphins - fully_trained_dolphins  # Calculate the number of remaining dolphins

    # Calculate the number of dolphins currently in training
    dolphins_in_training = (2/3) * remaining_dolphins

    # Calculate the number of dolphins that will be trained next month
    dolphins_next_month = remaining_dolphins - dolphins_in_training
    result = dolphins_next_month
    return result

print(solution())