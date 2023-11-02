def solution():
    # Calculate the number of kernels that popped in the first 30 seconds
    pop_first_30_seconds = 20

    # Calculate the number of kernels that popped in the next 30 seconds
    pop_next_30_seconds = 3 * pop_first_30_seconds

    # Calculate the number of kernels that popped in the next 30 seconds
    pop_next_30_seconds = 4 * pop_next_30_seconds

    # Calculate the number of kernels that popped in the final 30 seconds
    pop_final_30_seconds = 0.5 * pop_next_30_seconds

    # Calculate the total number of kernels that popped
    total_kernels = pop_first_30_seconds + pop_next_30_seconds + pop_next_30_seconds + pop_next_30_seconds + pop_final_30_seconds

    # Calculate the number of kernels that popped in the final 30 seconds
    pops_final_30_seconds = 0.25 * total_kernels

    result = pops_final_30_seconds
    return result

print(solution())