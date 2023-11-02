def solution():
    """It takes a dog groomer 10 minutes to dry a short-haired dog like a beagle.  It takes him twice as long to dry a full-haired, fluffy dog like a german shepherd.  One morning, he has 6 short-haired dogs to dry and 9 full-haired dogs to dry.  How many hours does it take him to dry all of the dogs?"""
    # Define the time to dry a short-haired dog and a full-haired dog
    SHORT_HAIR_TIME = 10
    FULL_HAIR_TIME = 2 * SHORT_HAIR_TIME

    # Define the number of short-haired and full-haired dogs
    short_hair_dogs = 6
    full_hair_dogs = 9

    # Calculate the total time to dry all the dogs
    total_time = short_hair_dogs * SHORT_HAIR_TIME + full_hair_dogs * FULL_HAIR_TIME

    # Convert the total time to hours
    hours = total_time / 60

    # Display the total time in hours
    result = hours
    return result

print(solution())