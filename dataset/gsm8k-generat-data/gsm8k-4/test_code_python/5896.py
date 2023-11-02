def solution():
    """There are 6 girls and 8 boys in the school play. If both parents of each kid attend the premiere, how many parents will be in the auditorium?"""
    # Calculate the total number of kids in the school play
    total_kids = 6 + 8

    # Calculate the total number of parents in the auditorium
    total_parents = 2 * total_kids

    # Return the result
    result = total_parents
    return result

print(solution())