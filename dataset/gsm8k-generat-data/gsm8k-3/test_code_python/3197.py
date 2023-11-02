def solution():
    """Anthony has 16 pets. This morning he forgot to lock the door and he lost 6 pets. After that 1/5 of his pets died from old age. How many pets does he have left?"""
    # Define the initial number of pets
    initial_pets = 16

    # Calculate the number of pets left after losing 6
    pets_after_loss = initial_pets - 6

    # Calculate the number of pets that die from old age
    old_age_deaths = int(pets_after_loss / 5)

    # Calculate the final number of pets
    final_pets = pets_after_loss - old_age_deaths

    # Display the final number of pets
    result = final_pets
    return result

print(solution())