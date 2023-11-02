def solution():
    """Baking in batches of 65 cupcakes, Carla made 45 batches of cupcakes for her daughter's birthday party. She then took 5 cupcakes from each batch, and fed them to her dogs. If Carla's daughter had 19 friends and they shared the remaining cupcakes equally among them, including the daughter, calculate the number of cupcakes that each of Carla's daughter's friends ate."""
    # Define the number of cupcakes in each batch and the number of batches
    BATCH_SIZE = 65
    NUM_BATCHES = 45

    # Calculate the total number of cupcakes before Carla feeds them to her dogs
    total_cupcakes = BATCH_SIZE * NUM_BATCHES

    # Calculate the number of cupcakes Carla feeds to her dogs
    cupcakes_to_dogs = NUM_BATCHES * 5

    # Calculate the number of cupcakes remaining for the daughter and her friends
    cupcakes_remaining = total_cupcakes - cupcakes_to_dogs

    # Calculate the number of cupcakes each friend can have, including the daughter
    cupcakes_per_person = cupcakes_remaining // 20

    # Display the number of cupcakes each friend can have
    result = cupcakes_per_person
    return result

print(solution())