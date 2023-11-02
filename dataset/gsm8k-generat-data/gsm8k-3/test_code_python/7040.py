def solution():
    """There are 20 dolphins in the aqua park. One-fourth of the dolphins are fully trained. Two-third of the remaining dolphins are currently in training and the rest will be trained next month. How many dolphins will be trained next month?"""
    
    # Calculate the number of fully trained dolphins
    fully_trained_dolphins = 20 / 4
    
    # Calculate the number of remaining dolphins
    remaining_dolphins = 20 - fully_trained_dolphins
    
    # Calculate the number of dolphins currently in training
    dolphins_in_training = (2/3) * remaining_dolphins
    
    # Calculate the number of dolphins that will be trained next month
    next_month_trained_dolphins = remaining_dolphins - dolphins_in_training
    
    # Display the number of dolphins to be trained next month
    result = next_month_trained_dolphins
    return result

print(solution())