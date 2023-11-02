def solution():
    # Calculate the number of new and broken crayons
    new_crayons = 120/3
    broken_crayons = 0.2 * 120

    # Calculate the number of slightly used crayons
    slightly_used_crayons = 120 - new_crayons - broken_crayons

    result = slightly_used_crayons
    return result

print(solution())