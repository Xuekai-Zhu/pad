def solution():
    num_children = 30

    # Calculate the number of women
    num_women = num_children * 3

    # Calculate the number of men
    num_men = num_women * 2

    # Calculate the total number of people in the group
    total_people = num_children + num_women + num_men
    result = total_people
    return result

print(solution())