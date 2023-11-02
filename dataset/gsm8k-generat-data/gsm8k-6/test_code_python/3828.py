def solution():
    # Calculate the number of women and children
    women = 50/2
    children = 50 - women - 15

    # Calculate the number of people who left during the movie screening
    men_left = 15/5
    children_left = 4
    total_left = men_left + children_left

    # Calculate the number of people who stayed
    stayed = 50 - total_left
    result = stayed
    return result

print(solution())