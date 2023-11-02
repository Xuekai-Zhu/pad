def solution():
    """Charles can earn $15 per hour when he housesits and $22 per hour when he walks a dog. If he housesits for 10 hours and walks 3 dogs, how many dollars will Charles earn?"""
    house_sitting_rate = 15
    dog_walking_rate = 22
    hours_house_sitting = 10
    num_dogs_walked = 3
    hours_dog_walking = num_dogs_walked * 1   # Assuming Charles walks each dog for 1 hour
    total_earnings = (house_sitting_rate * hours_house_sitting) + (dog_walking_rate * hours_dog_walking)
    result = total_earnings
    return result

print(solution())