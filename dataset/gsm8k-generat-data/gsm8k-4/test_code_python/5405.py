def solution():
    """Socorro is preparing for a math contest. She needs to train for a total of 5 hours. Each day, she answers problems about multiplication for 10 minutes and then division problems for 20 minutes. How many days will it take for her to complete her training?"""
    # Define the total training time in minutes
    total_training_time = 5 * 60

    # Define the time spent on multiplication and division problems each day
    multiplication_time = 10
    division_time = 20

    # Calculate the total time spent on one day of training
    daily_training_time = multiplication_time + division_time

    # Calculate the number of days it will take to complete the training
    days = total_training_time // daily_training_time

    # Return the result
    result = days
    return result

print(solution())