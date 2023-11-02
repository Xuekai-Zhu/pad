def solution():
    avocados_per_batch = 4  # Each batch requires 4 avocados
    servings_per_batch = 6  # Each batch serves about 6 people
    total_people = 42  # 42 people are going to be at the party including Allie

    # Calculate the total number of batches needed
    total_batches = total_people / servings_per_batch

    # Calculate the total number of avocados needed
    total_avocados = total_batches * avocados_per_batch
    result = total_avocados
    return result

print(solution())