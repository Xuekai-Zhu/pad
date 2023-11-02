def solution():
    hours_housesitting = 10
    rate_housesitting = 15

    num_dogs_walked = 3
    rate_dog_walking = 22

    # Calculate the total amount earned from housesitting
    total_housesitting_earned = hours_housesitting * rate_housesitting

    # Calculate the total amount earned from dog walking
    total_dog_walking_earned = num_dogs_walked * rate_dog_walking

    # Calculate the total amount earned
    total_earned = total_housesitting_earned + total_dog_walking_earned
    result = total_earned
    return result

print(solution())