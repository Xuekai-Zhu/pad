def solution():
    """Charles can earn $15 per hour when he housesits and $22 per hour when he walks a dog. 
    If he housesits for 10 hours and walks 3 dogs, how many dollars will Charles earn?"""
    # Define the hourly rates for housesitting and dog walking
    HOUSESITTING_RATE = 15
    DOG_WALKING_RATE = 22

    # Calculate the total earnings from housesitting
    housesitting_earnings = HOUSESITTING_RATE * 10

    # Calculate the total earnings from dog walking
    dog_walking_earnings = DOG_WALKING_RATE * 3

    # Calculate the total earnings
    total_earnings = housesitting_earnings + dog_walking_earnings

    # return the result
    result = total_earnings
    return result

print(solution())