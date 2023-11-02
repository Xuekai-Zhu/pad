def solution():
    boxes = 12
    samples_per_box = 20
    left_over_samples = 5

    # Calculate the total number of samples given out
    total_samples = (boxes * samples_per_box) - left_over_samples

    # Calculate the number of customers who tried a sample
    num_customers = total_samples / 1  # assuming each customer had only one sample

    result = num_customers
    return result

print(solution())