def solution():
    num_batches = 5
    batch_size = 80
    defect_rate = 0.25

    # Calculate the total number of engines
    total_engines = num_batches * batch_size

    # Calculate the number of defective engines
    num_defective = total_engines * defect_rate

    # Calculate the number of non-defective engines
    num_non_defective = total_engines - num_defective
    result = num_non_defective
    return result

print(solution())