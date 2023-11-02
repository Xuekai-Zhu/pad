def solution():
    cat_owners = 30  # 30 citizens own a cat
    dog_owners = 0.5 * 0.6  # Half of pet owners own dogs, which is 60% of the population
    total_pet_owners = cat_owners / 0.2  # Assuming 20% of pet owners own only cats

    # Calculate the total population
    total_population = total_pet_owners / 0.6  # 60% of the population owns pets

    result = total_population
    return result

print(solution())