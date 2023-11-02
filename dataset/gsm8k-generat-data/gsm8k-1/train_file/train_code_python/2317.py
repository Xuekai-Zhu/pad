def solution():
    """It takes a dog groomer 10 minutes to dry a short-haired dog like a beagle. It takes him twice as long to dry a full-haired, fluffy dog like a german shepherd. One morning, he has 6 short-haired dogs to dry and 9 full-haired dogs to dry. How many hours does it take him to dry all of the dogs?"""
    sh_dog_time = 10 # in minutes
    fh_dog_time = 2 * sh_dog_time # in minutes
    total_time = (sh_dog_time * 6) + (fh_dog_time * 9) # in minutes
    total_time_in_hours = total_time / 60 # convert to hours
    result = total_time_in_hours
    return result

print(solution())