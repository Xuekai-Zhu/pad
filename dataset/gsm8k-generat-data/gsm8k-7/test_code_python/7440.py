def solution():
    num_cupcakes_per_batch = 65
    num_batches = 45
    cupcakes_taken_by_dogs = 5
    num_friends = 19

    # Calculate the total number of cupcakes Carla baked
    total_cupcakes = num_cupcakes_per_batch * num_batches

    # Subtract the cupcakes taken by dogs
    total_cupcakes -= cupcakes_taken_by_dogs * num_batches

    # Calculate the number of cupcakes each friend will get, including Carla's daughter
    cupcakes_per_person = total_cupcakes / (num_friends + 1)

    result = cupcakes_per_person
    return result

print(solution())