def solution():
    """It takes Jennifer 20 minutes to groom each of her 2 long hair dachshunds.  If she grooms her dogs every day, how many hours does she spend grooming her dogs in 30 days?"""
    # Define the time it takes Jennifer to groom one dog
    GROOMING_TIME = 20 # in minutes

    # Define the number of dogs Jennifer has
    NUM_DOGS = 2

    # Calculate the total grooming time in minutes
    total_grooming_time = GROOMING_TIME * NUM_DOGS * 30

    # Convert the total grooming time to hours
    total_grooming_hours = total_grooming_time / 60

    # Display the total grooming hours
    result = total_grooming_hours
    return result

print(solution())