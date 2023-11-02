def solution():
    # Initialize variables for number of bones each dog carried
    dog_1 = 3
    dog_2 = dog_1 - 1
    dog_3 = 2 * dog_2
    dog_4 = 1
    dog_5 = 2 * dog_4

    # Calculate the total number of bones in the original pile
    total_bones = dog_1 + dog_2 + dog_3 + dog_4 + dog_5
    result = total_bones
    return result

print(solution())