def solution():
    """Anthony has 16 pets. This morning he forgot to lock the door and he lost 6 pets. After that 1/5 of his pets died from old age. How many pets does he have left?"""
    # Define the initial number of pets
    initial_pets = 16

    # Calculate the number of pets that are left after losing 6
    pets_left = initial_pets - 6

    # Calculate the number of pets that died from old age
    dead_pets = pets_left // 5

    # Calculate the final number of pets
    final_pets = pets_left - dead_pets

    # return the result
    result = final_pets
    return result

print(solution())