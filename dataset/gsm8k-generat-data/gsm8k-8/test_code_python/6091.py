def solution():
    # Calculate the total number of samples available
    total_samples = 12 * 20

    # Calculate the number of samples that were not taken
    leftover_samples = 5

    # Calculate the number of samples that were taken
    taken_samples = total_samples - leftover_samples

    # Calculate the number of customers who tried a sample
    customers_tried_sample = taken_samples / 1
    result = customers_tried_sample
    return result

print(solution())