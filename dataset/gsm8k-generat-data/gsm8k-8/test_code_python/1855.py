def solution():
    # Define the percentage of pet owners and the percentage of dog owners
    pet_owners_percentage = 0.6
    dog_owners_percentage = 0.5

    # Calculate the total number of pet owners and dog owners
    total_pet_owners = 0.6 * 100
    total_dog_owners = 0.5 * total_pet_owners

    # Calculate the number of cat owners
    cat_owners = 30

    # Calculate the total number of citizens
    total_citizens = cat_owners / (1 - (total_dog_owners / total_pet_owners))
    result = total_citizens
    return result

print(solution())