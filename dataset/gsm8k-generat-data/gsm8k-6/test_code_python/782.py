def solution():
    # Calculate the maximum number of dresses Melissa can make
    max_dresses = 56 // 4  # each dress takes 4 square meters of fabric
    # Calculate the total time required to make the maximum number of dresses
    total_time = max_dresses * 3  # each dress takes 3 hours to make
    result = total_time
    return result

print(solution())