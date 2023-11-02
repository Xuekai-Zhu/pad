def solution():
    total_insects = 200 + 300 #total number of insects collected
    num_groups = 4 #number of groups to divide the insects equally among

    # Calculate the number of insects each group gets
    num_insects_per_group = total_insects / num_groups
    result = num_insects_per_group
    return result

print(solution())