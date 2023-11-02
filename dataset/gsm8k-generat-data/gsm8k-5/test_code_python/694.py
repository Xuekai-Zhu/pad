def solution():
    batch_size = 80  # Each batch contains 80 engines
    num_batches = 5  # Total of 5 batches

    # Calculate the total number of engines in all batches
    total_engines = batch_size * num_batches

    # Calculate the number of defective engines
    num_defective_engines = total_engines // 4

    # Calculate the number of non-defective engines
    num_nondefective_engines = total_engines - num_defective_engines
    result = num_nondefective_engines
    return result

print(solution())