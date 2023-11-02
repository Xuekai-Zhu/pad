def solution():
    """There are 20 dolphins in the aqua park. One-fourth of the dolphins are fully trained. Two-third of the remaining dolphins are currently in training and the rest will be trained next month. How many dolphins will be trained next month?"""
    total_dolphins = 20
    trained_dolphins = total_dolphins / 4
    remaining_dolphins = total_dolphins - trained_dolphins
    in_training_dolphins = (2 / 3) * remaining_dolphins
    dolphins_to_train_next_month = remaining_dolphins - in_training_dolphins
    result = dolphins_to_train_next_month
    return result

print(solution())