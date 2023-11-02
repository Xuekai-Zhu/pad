def solution():
    # Calculate the number of leaves shed in the first week
    leaves_shed_week1 = (2/5) * 1000
    remaining_leaves_week1 = 1000 - leaves_shed_week1

    # Calculate the number of leaves shed in the second week
    leaves_shed_week2 = 0.4 * remaining_leaves_week1
    remaining_leaves_week2 = remaining_leaves_week1 - leaves_shed_week2

    # Calculate the number of leaves shed in the third week
    leaves_shed_week3 = (3/4) * leaves_shed_week2
    remaining_leaves_week3 = remaining_leaves_week2 - leaves_shed_week3

    result = remaining_leaves_week3
    return result

print(solution())