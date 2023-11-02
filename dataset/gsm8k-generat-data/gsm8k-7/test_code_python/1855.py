def solution():
    pet_owners_percent = 0.6
    dog_owners_percent = 0.5
    cat_owners = 30

    # Calculate the total number of pet owners
    total_pet_owners = cat_owners / (pet_owners_percent * dog_owners_percent)

    # Calculate the total population of the town
    total_population = total_pet_owners / pet_owners_percent
    result = total_population
    return result

print(solution())