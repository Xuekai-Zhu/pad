def solution():
    boxes = 12  # The store opened 12 boxes of samples
    box_size = 20  # Each box contained 20 samples
    leftover_samples = 5  # There were 5 samples left over at the end of the day

    # Calculate the total number of samples given out
    total_samples = (boxes * box_size) - leftover_samples

    # Calculate the number of customers who tried a sample (assuming one sample per person)
    customers = total_samples

    result = customers
    return result

print(solution())