def solution():
    # Define the time it takes to paint each flower
    lily_time = 5
    rose_time = 7
    orchid_time = 3
    vine_time = 2

    # Calculate the total time it will take to paint each type of flower
    total_lily_time = lily_time * 17
    total_rose_time = rose_time * 10
    total_orchid_time = orchid_time * 6
    total_vine_time = vine_time * 20

    # Calculate the total time it will take to paint all the flowers
    total_time = total_lily_time + total_rose_time + total_orchid_time + total_vine_time
    result = total_time
    return result

print(solution())