def solution():
    """There are 14 girls, 11 boys, and their parents at a park. If they split into 3 equally sized playgroups, each group contains 25 people. How many parents were at the park?"""
    # Define the total number of children
    total_children = 14 + 11

    # Define the total number of people at the park
    total_people = total_children + (total_children / 2)

    # Calculate the number of parents at the park
    parents = total_people - (3 * 25)

    # return the result
    result = parents
    return result

print(solution())