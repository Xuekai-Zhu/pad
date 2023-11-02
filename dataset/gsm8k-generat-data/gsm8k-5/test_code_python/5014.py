def solution():
    # Time taken to paint different flowers
    lily_time = 5  # minutes
    rose_time = 7  # minutes
    orchid_time = 3  # minutes
    vine_time = 2  # minutes

    # Number of flowers to be painted
    lilies = 17
    roses = 10
    orchids = 6
    vines = 20

    # Calculate the total time to paint all the flowers
    total_time = (lily_time * lilies) + (rose_time * roses) + (orchid_time * orchids) + (vine_time * vines)
    result = total_time
    return result

print(solution())