def solution():
    num_spotted_dogs = 15
    spotted_dogs_ratio = 0.5
    pointy_ears_ratio = 0.2  # 1/5

    # Calculate the total number of dogs at the park
    total_dogs = num_spotted_dogs / spotted_dogs_ratio

    # Calculate the number of dogs with pointy ears
    num_pointy_ears_dogs = total_dogs * pointy_ears_ratio
    result = num_pointy_ears_dogs
    return result

print(solution())