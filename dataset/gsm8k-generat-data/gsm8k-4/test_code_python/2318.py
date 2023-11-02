def solution():
    """It takes a dog groomer 10 minutes to dry a short-haired dog like a beagle. It takes him twice as long to dry a full-haired, fluffy dog like a german shepherd. One morning, he has 6 short-haired dogs to dry and 9 full-haired dogs to dry. How many hours does it take him to dry all of the dogs?"""
    # Define the time to dry a short-haired dog and a full-haired dog
    short_hair_duration = 10  # in minutes
    full_hair_duration = 2 * short_hair_duration  # in minutes

    # Define the number of short-haired dogs and full-haired dogs
    num_short_hair_dogs = 6
    num_full_hair_dogs = 9

    # Calculate the total time to dry all dogs
    total_duration = num_short_hair_dogs * short_hair_duration + num_full_hair_dogs * full_hair_duration

    # Convert the duration to hours
    total_hours = total_duration / 60

    result = total_hours
    return result

print(solution())