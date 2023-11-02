def solution():
    cupcakes_per_batch = 65  # Carla makes 65 cupcakes per batch
    batches = 45  # Carla makes 45 batches of cupcakes
    cupcakes_total = cupcakes_per_batch * batches  # Total number of cupcakes Carla makes
    cupcakes_given_to_dogs = 5 * batches  # Number of cupcakes Carla gave to her dogs
    cupcakes_remaining = cupcakes_total - cupcakes_given_to_dogs  # Number of cupcakes remaining after feeding the dogs
    daughter_and_friends = 19 + 1  # Carla's daughter and her 19 friends
    cupcakes_per_person = cupcakes_remaining // daughter_and_friends  # Integer division to calculate number of cupcakes each person gets
    result = cupcakes_per_person
    return result

print(solution())