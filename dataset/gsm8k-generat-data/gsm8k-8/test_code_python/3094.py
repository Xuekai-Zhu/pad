def solution():
    # Define the number of cups and rates of painting
    rose_cups = 6
    lily_cups = 14
    rose_rate = 6
    lily_rate = 7

    # Calculate the total time to paint the cups
    total_time = rose_cups / rose_rate + lily_cups / lily_rate

    # Calculate the hourly rate
    hourly_rate = 90 / total_time
    result = hourly_rate
    return result

print(solution())