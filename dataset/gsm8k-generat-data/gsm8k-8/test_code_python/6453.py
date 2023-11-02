def solution():
    # Define the number of people and avocados per batch
    num_people = 42
    avocados_per_batch = 4
    servings_per_batch = 6

    # Calculate the number of batches needed
    num_batches = num_people / servings_per_batch

    # Calculate the total number of avocados needed
    total_avocados = num_batches * avocados_per_batch
    result = total_avocados
    return result

print(solution())