def solution():
    """Parker wants to find out what the average percentage of kernels that pop in a bag is. In the first bag he makes, 60 kernels pop and the bag has 75 kernels. In the second bag, 42 kernels pop and there are 50 in the bag. In the final bag, 82 kernels pop and the bag has 100 kernels."""
    total_popped_kernels = 60 + 42 + 82
    total_kernels = 75 + 50 + 100
    percentage_popped = (total_popped_kernels / total_kernels) * 100
    result = percentage_popped
    return result

print(solution())