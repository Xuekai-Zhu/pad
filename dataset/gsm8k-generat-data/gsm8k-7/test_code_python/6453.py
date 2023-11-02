def solution():
    avocados_per_batch = 4
    served_per_batch = 6
    total_people = 42
    allie = 1  # Including herself

    # Calculate the total number of batches needed
    total_batches = (total_people - allie) / served_per_batch

    # Calculate the total number of avocados needed
    total_avocados = total_batches * avocados_per_batch
    result = total_avocados
    return result

print(solution())