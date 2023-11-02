def solution():
    # Define the number of children
    children = 30

    # Calculate the number of women
    women = children * 3

    # Calculate the number of men
    men = women * 2

    # Calculate the total number of people in the group
    total_people = children + women + men
    result = total_people
    return result

print(solution())