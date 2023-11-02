def solution():
    # Count the number of parents for each kid
    parents_per_kid = 2

    # Calculate the total number of kids in the play
    total_kids = 6 + 8

    # Calculate the total number of parents
    total_parents = total_kids * parents_per_kid

    result = total_parents
    return result

print(solution())