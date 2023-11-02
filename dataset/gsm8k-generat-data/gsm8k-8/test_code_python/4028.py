def solution():
    # Calculate the total number of available pet beds after adding 8 more
    total_pet_beds = 12 + 8

    # Calculate the maximum number of pets that can be accommodated based on the parent's argument
    max_num_of_pets = total_pet_beds // 2

    result = max_num_of_pets
    return result

print(solution())