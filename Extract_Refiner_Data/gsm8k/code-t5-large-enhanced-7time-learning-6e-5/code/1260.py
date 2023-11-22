def solution():
    
    # Calculate the number of kernels popped in the first 30 seconds
    first_30_seconds = 20

    # Calculate the number of kernels popped in the next 30 seconds
    next_30_seconds = first_30_seconds * 3

    # Calculate the number of kernels popped in the next thirty seconds
    next_thirty_seconds = next_30_seconds * 4

    # Calculate the number of kernels popped in the final 30 seconds
    final_30_seconds = next_thirty_seconds / 2

    # Calculate the total number of kernels popped
    total_kernels_popped = first_30_seconds + next_30_seconds + next_thirty_seconds + final_30_seconds

    # Calculate the number of kernels popped in the final 30 seconds
    final_30_seconds = final_30_seconds / 4

    # Calculate the number of kernels popped in the final quarter of the final 30 seconds
    final_quarter_popped = final_30_seconds / 4

    # Calculate the total number of kernels popped
    total

print(solution())