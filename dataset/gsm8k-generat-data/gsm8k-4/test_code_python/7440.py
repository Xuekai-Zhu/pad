def solution():
    """Baking in batches of 65 cupcakes, Carla made 45 batches of cupcakes for her daughter's birthday party. She then took 5 cupcakes from each batch, and fed them to her dogs. If Carla's daughter had 19 friends and they shared the remaining cupcakes equally among them, including the daughter, calculate the number of cupcakes that each of Carla's daughter's friends ate."""
    # Define the initial number of cupcakes
    initial_cupcakes = 65 * 45

    # Calculate the number of cupcakes taken by Carla for the dogs
    dog_cupcakes = 5 * 45

    # Calculate the number of remaining cupcakes after feeding the dogs
    remaining_cupcakes = initial_cupcakes - dog_cupcakes

    # Calculate the number of cupcakes per person, including the daughter
    cupcakes_per_person = remaining_cupcakes // 20

    # Return the result
    result = cupcakes_per_person
    return result

print(solution())