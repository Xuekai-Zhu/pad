def solution():
    """There are 20 dolphins in the aqua park. One-fourth of the dolphins are fully trained. Two-third of the remaining dolphins are currently in training and the rest will be trained next month. How many dolphins will be trained next month?"""
    total_dolphins = 20
    fully_trained = total_dolphins // 4
    remaining_dolphins = total_dolphins - fully_trained
    training_now = (2/3) * remaining_dolphins
    training_next_month = remaining_dolphins - training_now
    result = training_next_month
    return result

print(solution())