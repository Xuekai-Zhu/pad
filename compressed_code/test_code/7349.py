def solution():
    
    house_sitting_rate = 15
    dog_walking_rate = 22
    hours_house_sitting = 10
    num_dogs_walked = 3
    hours_dog_walking = num_dogs_walked * 1   
    total_earnings = (house_sitting_rate * hours_house_sitting) + (dog_walking_rate * hours_dog_walking)
    result = total_earnings
    return result

print(solution())