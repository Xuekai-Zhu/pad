def solution():
    """Rylee is bored and decides to count the number of leaves falling off the tree in her backyard. 7 leaves fall in the first hour. For the second and third hour, the leaves fall at a rate of 4 per hour. What is the average number of leaves which fell per hour?"""
    leaves_hour_1 = 7
    leaves_hour_2 = 4
    leaves_hour_3 = 4
    total_leaves = leaves_hour_1 + leaves_hour_2 + leaves_hour_3
    average_leaves = total_leaves / 3
    result = average_leaves
    return result

print(solution())