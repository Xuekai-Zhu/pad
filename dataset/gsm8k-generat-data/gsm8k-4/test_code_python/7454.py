def solution():
    """It takes Jennifer 20 minutes to groom each of her 2 long hair dachshunds. If she grooms her dogs every day, how many hours does she spend grooming her dogs in 30 days?"""
    # Define the time it takes to groom one dog
    TIME_PER_DOG = 20  # minutes

    # Define the number of dogs Jennifer has
    NUM_DOGS = 2

    # Define the number of days
    NUM_DAYS = 30

    # Calculate the total time spent grooming in minutes
    total_time = TIME_PER_DOG * NUM_DOGS * NUM_DAYS

    # Convert the time to hours
    total_time_hours = total_time / 60

    # Round the result to two decimal places
    result = round(total_time_hours, 2)
    return result

print(solution())