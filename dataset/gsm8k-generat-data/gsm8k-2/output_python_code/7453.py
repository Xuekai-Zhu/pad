def solution():
    """It takes Jennifer 20 minutes to groom each of her 2 long hair dachshunds. If she grooms her dogs every day, how many hours does she spend grooming her dogs in 30 days?"""
    minutes_per_dog = 20
    dogs = 2
    days = 30
    minutes_per_day = minutes_per_dog * dogs
    total_minutes = minutes_per_day * days
    hours = total_minutes / 60
    result = hours
    return result

print(solution())