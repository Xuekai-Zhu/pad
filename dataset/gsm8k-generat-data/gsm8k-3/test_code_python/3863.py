def solution():
    """It takes 2.5 hours to groom a dog and 0.5 hours to groom a cat. What is the number of minutes it takes to groom 5 dogs and 3 cats?"""
    # Define the time it takes to groom a dog and a cat
    DOG_TIME = 2.5
    CAT_TIME = 0.5

    # Define the number of dogs and cats to groom
    NUM_DOGS = 5
    NUM_CATS = 3

    # Calculate the total time to groom all the dogs and cats
    total_time = (NUM_DOGS * DOG_TIME) + (NUM_CATS * CAT_TIME)

    # Convert the total time to minutes
    total_time_minutes = total_time * 60

    # Display the total time in minutes
    result = total_time_minutes
    return result

print(solution())