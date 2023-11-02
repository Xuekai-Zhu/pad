def solution():
    total_insects = 200 + 300  # Total number of insects collected
    num_groups = 4  # Number of groups to divide the insects into
    
    # Calculate the number of insects each group gets
    insects_per_group = total_insects // num_groups
    result = insects_per_group
    return result

print(solution())