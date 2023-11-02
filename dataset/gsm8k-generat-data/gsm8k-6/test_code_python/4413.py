def solution():
    # Calculate the total number of siblings Billy has
    total_siblings = 2 + (2 * 2)  # Billy has twice as many brothers as sisters, and he has 2 sisters

    # Calculate the number of sodas each sibling can have
    sodas_per_sibling = 12 // total_siblings  # divide the total sodas by the number of siblings

    result = sodas_per_sibling
    return result

print(solution())