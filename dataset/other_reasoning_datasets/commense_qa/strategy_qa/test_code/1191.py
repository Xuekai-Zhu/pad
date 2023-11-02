def solution():
    # Define the relationship between reptiles, crickets, and pet ownership
    reptiles_are_popular_pets = True
    reptiles_enjoy_eating_crickets = True
    crickets_are_sold_at_pet_stores = True
    if reptiles_are_popular_pets and reptiles_enjoy_eating_crickets and crickets_are_sold_at_pet_stores:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())