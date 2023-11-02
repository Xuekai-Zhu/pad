def solution():
    """There are 20 dolphins in the aqua park. One-fourth of the dolphins are fully trained. Two-third of the remaining dolphins are currently in training and the rest will be trained next month. How many dolphins will be trained next month?"""
    # Define the total number of dolphins
    total_dolphins = 20

    # Calculate the number of fully trained dolphins
    fully_trained_dolphins = total_dolphins // 4

    # Calculate the remaining number of dolphins
    remaining_dolphins = total_dolphins - fully_trained_dolphins

    # Calculate the number of dolphins currently in training
    in_training_dolphins = (remaining_dolphins * 2) // 3
    
    # Calculate the number of dolphins that will be trained next month
    next_month_dolphins = remaining_dolphins - in_training_dolphins
    
    result = next_month_dolphins
    return result

print(solution())