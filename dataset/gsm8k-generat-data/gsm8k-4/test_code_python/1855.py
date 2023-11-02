def solution():
    """In a town where 60% of the citizens own a pet, half own a dog and 30 own a cat. How many citizens are in the town?"""
    # Define the percentage of citizens who own pets
    pet_owners_percentage = 60

    # Define the percentage of pet owners who own dogs
    dog_owners_percentage = 50

    # Calculate the percentage of pet owners who own cats
    cat_owners_percentage = (pet_owners_percentage - dog_owners_percentage) / 2

    # Calculate the total number of cat owners
    total_cat_owners = 30

    # Calculate the total number of pet owners
    total_pet_owners = (100 / pet_owners_percentage) * total_cat_owners / (cat_owners_percentage / 100)

    # Calculate the total number of citizens
    total_citizens = (100 / pet_owners_percentage) * total_pet_owners

    # return the result
    result = round(total_citizens)
    return result

print(solution())