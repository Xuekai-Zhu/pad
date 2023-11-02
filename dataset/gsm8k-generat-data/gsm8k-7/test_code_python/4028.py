def solution():
    initial_pet_beds = 12
    additional_pet_beds = 8
    pet_beds_per_pet = 2

    # Calculate the total number of pet beds Lucas has after adding the additional ones
    total_pet_beds = initial_pet_beds + additional_pet_beds

    # Calculate the maximum number of pets Lucas can have based on the number of available pet beds
    max_num_pets = total_pet_beds / pet_beds_per_pet
    result = max_num_pets
    return result

print(solution())