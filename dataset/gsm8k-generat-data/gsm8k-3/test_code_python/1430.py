def solution():
    """There are 14 girls, 11 boys, and their parents at a park. If they split into 3 equally sized playgroups, each group contains 25 people. How many parents were at the park?"""
    # Calculate the total number of people at the park
    total_people = 14 + 11 + 2*25*3

    # Calculate the number of parents at the park
    num_parents = total_people - 14 - 11

    # Display the number of parents at the park
    result = num_parents
    return result

print(solution())