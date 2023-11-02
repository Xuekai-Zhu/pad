def solution():
    # Calculate the total number of siblings Billy has
    num_siblings = 2 * 2              # 2 sisters, each with 2 brothers

    # Calculate the number of sodas each sibling can have if they all get an equal amount
    sodas_per_sibling = 12 / (num_siblings + 1)     # Billy also gets a soda

    result = sodas_per_sibling
    return result

print(solution())