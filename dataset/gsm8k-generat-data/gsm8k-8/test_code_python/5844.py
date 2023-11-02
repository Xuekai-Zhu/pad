def solution():
    # Set up variables for the first odd integer, the sum, and the counter
    n = -49
    sum = -147
    count = 1

    # Loop through until the sum is exceeded and increment the counter each time
    while sum < 0:
        n += 2
        sum += n
        count += 1

    # Calculate the largest number (which is the last odd integer in the consecutive series)
    largest_num = n - 2
    result = largest_num
    return result

print(solution())