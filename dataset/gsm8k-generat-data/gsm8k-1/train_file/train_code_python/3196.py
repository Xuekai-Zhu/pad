def solution():
    """Anthony has 16 pets. This morning he forgot to lock the door and he lost 6 pets. After that 1/5 of his pets died from old age. How many pets does he have left?"""
    starting_pets = 16
    lost_pets = 6
    remaining_pets = starting_pets - lost_pets
    percent_loss = 1/5
    pets_died = remaining_pets * percent_loss
    pets_left = remaining_pets - pets_died
    result = pets_left
    return result

print(solution())