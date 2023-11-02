def solution():
    emery_time = 20 / 5  # Emery reads 5 times faster than Serena, so she takes 1/5 the time
    serena_time = 20  # Serena takes 20 days to read the book
    total_time = emery_time + serena_time  # Calculate the total time taken by both

    # Calculate the average time taken by both by dividing the total time by 2
    average_time = total_time / 2
    result = average_time
    return result

print(solution())