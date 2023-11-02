def solution():
    """A dog is being treated for fleas. One flea treatment gets rid of half the fleas. After four treatments, the dog has 14 fleas left. How many more fleas did the dog have before the flea treatments than after?"""
    # Define the initial number of fleas
    initial_fleas = None

    # Define the final number of fleas
    final_fleas = 14

    # Calculate the number of fleas the dog had before the flea treatments
    for i in range(4):
        final_fleas *= 2
    initial_fleas = final_fleas - 14

    result = initial_fleas - final_fleas
    return result

print(solution())