def solution():
    # Calculate the number of women
    women = 60 / 2

    # Calculate the number of children
    children = 60 - women - 15

    # Calculate the number of men who left
    men_left = 15 / 3

    # Calculate the number of children who left
    children_left = 5

    # Calculate the number of people who stayed
    stayed = women + children - children_left - men_left

    result = stayed
    return result

print(solution())