def solution():
    """Rylee is bored and decides to count the number of leaves falling off the tree in her backyard. 7 leaves fall in the first hour. For the second and third hour, the leaves fall at a rate of 4 per hour. What is the average number of leaves which fell per hour?"""
    total_leaves = 7 + (2 * 4)
    average_leaves = total_leaves / 3
    result = average_leaves
    return result

print(solution())