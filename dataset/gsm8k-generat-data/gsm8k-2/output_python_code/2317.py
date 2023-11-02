def solution():
    """It takes a dog groomer 10 minutes to dry a short-haired dog like a beagle. It takes him twice as long to dry a full-haired, fluffy dog like a german shepherd. One morning, he has 6 short-haired dogs to dry and 9 full-haired dogs to dry. How many hours does it take him to dry all of the dogs?"""
    short_hair_dog_time = 10
    full_hair_dog_time = 2 * short_hair_dog_time
    num_short_hair_dogs = 6
    num_full_hair_dogs = 9
    total_time = (short_hair_dog_time * num_short_hair_dogs) + (full_hair_dog_time * num_full_hair_dogs)
    total_hours = total_time / 60.0
    result = total_hours
    return result

print(solution())