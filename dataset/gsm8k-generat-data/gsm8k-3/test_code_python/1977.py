def solution():
    """Charles can earn $15 per hour when he housesits and $22 per hour when he walks a dog. If he housesits for 10 hours and walks 3 dogs, how many dollars will Charles earn?"""
    # Define the hourly rates
    HOUSESITTING_RATE = 15
    DOG_WALKING_RATE = 22

    # Define the number of hours spent housesitting and dog walking
    housesitting_hours = 10
    dog_walking_hours = 3

    # Calculate Charles' earnings
    housesitting_earnings = housesitting_hours * HOUSESITTING_RATE
    dog_walking_earnings = dog_walking_hours * DOG_WALKING_RATE
    total_earnings = housesitting_earnings + dog_walking_earnings

    # Display Charles' earnings
    result = total_earnings
    return result

print(solution())