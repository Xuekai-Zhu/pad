def solution():
    """It takes Jennifer 20 minutes to groom each of her 2 long hair dachshunds. If she grooms her dogs every day, how many hours does she spend grooming her dogs in 30 days?"""
    dogs_groomed_per_day = 2
    minutes_per_dog = 20
    days = 30
    total_minutes = dogs_groomed_per_day * minutes_per_dog * days
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())