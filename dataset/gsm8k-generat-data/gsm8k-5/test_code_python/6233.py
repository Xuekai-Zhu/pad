def solution():
    total_children = 50  # There are 50 children at the party
    boys_ratio = 3/5  # Three-fifths of the children are boys

    # Calculate the number of boys and girls
    boys = total_children * boys_ratio
    girls = total_children - boys

    result = girls
    return result

print(solution())