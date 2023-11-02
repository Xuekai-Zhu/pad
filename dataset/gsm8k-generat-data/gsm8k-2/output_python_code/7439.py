def solution():
    """Baking in batches of 65 cupcakes, Carla made 45 batches of cupcakes for her daughter's birthday party.
    She then took 5 cupcakes from each batch, and fed them to her dogs.
    If Carla's daughter had 19 friends and they shared the remaining cupcakes equally among them, including the daughter,
    calculate the number of cupcakes that each of Carla's daughter's friends ate."""
    batch_size = 65
    num_batches = 45
    removed_cupcakes = 5 * num_batches
    total_cupcakes = batch_size * num_batches
    remaining_cupcakes = total_cupcakes - removed_cupcakes
    num_people = 19 + 1  # 1 for Carla's daughter
    cupcakes_per_person = remaining_cupcakes // num_people
    result = cupcakes_per_person
    return result

print(solution())