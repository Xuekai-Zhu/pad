def solution():
    children = 30  # given that the number of children is 30
    women = 3 * children  # given that the number of women is 3 times the number of children
    men = 2 * women  # given that the number of men is twice the number of women
    total_people = children + women + men  # total number of people in the group
    result = total_people
    return result

print(solution())