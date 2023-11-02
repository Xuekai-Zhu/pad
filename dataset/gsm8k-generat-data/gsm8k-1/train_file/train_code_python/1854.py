def solution():
    """In a town where 60% of the citizens own a pet, half own a dog and 30 own a cat. How many citizens are in the town?"""
    pet_owners_percent = 60
    dog_owners_percent = 50
    cat_owners = 30
    total_citizens = cat_owners / (1 / (pet_owners_percent / 100)) / (dog_owners_percent / 100)
    result = total_citizens
    return result

print(solution())