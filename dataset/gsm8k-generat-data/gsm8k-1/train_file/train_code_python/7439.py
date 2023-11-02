def solution():
    """Baking in batches of 65 cupcakes, Carla made 45 batches of cupcakes for her daughter's birthday party. She then took 5 cupcakes from each batch, and fed them to her dogs. If Carla's daughter had 19 friends and they shared the remaining cupcakes equally among them, including the daughter, calculate the number of cupcakes that each of Carla's daughter's friends ate."""
    cupcakes_per_batch = 65
    batches = 45
    cupcakes_before_dogs = cupcakes_per_batch * batches
    cupcakes_after_dogs = cupcakes_before_dogs - (5 * batches)
    num_people = 19 + 1 # 1 is for Carla's daughter
    cupcakes_per_person = cupcakes_after_dogs // num_people
    result = cupcakes_per_person
    return result

print(solution())