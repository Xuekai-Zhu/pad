def solution():
    # Calculate the number of times Rick needs to divide his books into equal groups of 2
    num_groups = 1
    while 400 / (2 ** num_groups) > 24:
        num_groups += 1
    result = num_groups
    return result

print(solution())