def solution():
    emery_speed = 5  # Emery reads 5 times faster than Serena
    serena_time = 20  # Time it takes for Serena to read the book

    # Calculate the time it takes for Emery to read the book
    emery_time = serena_time / emery_speed

    # Calculate the total time it takes for both of them to read the book
    total_time = serena_time + emery_time

    # Calculate the average time it takes for both of them to read the book
    avg_time = total_time / 2
    result = avg_time
    return result

print(solution())