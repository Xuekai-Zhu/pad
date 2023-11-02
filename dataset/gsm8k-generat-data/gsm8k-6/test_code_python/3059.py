def solution():
    # Calculate the weight of each dog
    brown_dog_weight = 4
    black_dog_weight = brown_dog_weight + 1
    white_dog_weight = brown_dog_weight * 2
    grey_dog_weight = black_dog_weight - 2
    
    # Calculate the total weight of all dogs
    total_weight = brown_dog_weight + black_dog_weight + white_dog_weight + grey_dog_weight
    
    # Calculate the average weight of all dogs
    average_weight = total_weight / 4
    result = average_weight
    return result

print(solution())