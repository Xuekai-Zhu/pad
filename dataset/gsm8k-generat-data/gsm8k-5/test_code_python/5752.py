def solution():
    children = 30  # Given, the number of children is 30
    women = children * 3  # The number of women is 3 times the number of children
    men = women * 2  # The number of men is twice the number of women
    total_people = children + women + men  # Total number of people in the group

    result = total_people
    return result

print(solution())