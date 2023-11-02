def solution():
    # Calculate the total number of samples available
    total_samples = 12 * 20 + 5  # 12 boxes were opened, each containing 20 samples, with 5 left over

    # Calculate the number of customers who tried a sample
    num_customers = total_samples - 5  # subtract the remaining 5 samples
    result = num_customers
    return result

print(solution())