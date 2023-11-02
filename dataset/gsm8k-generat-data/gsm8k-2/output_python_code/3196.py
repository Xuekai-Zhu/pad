def solution():
    """Anthony has 16 pets. This morning he forgot to lock the door and he lost 6 pets. After that 1/5 of his pets died from old age. How many pets does he have left?"""
    initial_pets = 16
    lost_pets = 6
    remaining_pets = initial_pets - lost_pets
    old_age_deaths = remaining_pets // 5
    final_pets = remaining_pets - old_age_deaths
    result = final_pets
    return result

print(solution())