def solution():
    # Define the number of crayons as variables
    total_crayons = 120
    new_crayons = total_crayons / 3
    broken_crayons = 0.2 * total_crayons

    # Calculate the number of slightly used crayons
    slightly_used_crayons = total_crayons - new_crayons - broken_crayons
    result = slightly_used_crayons
    return result

print(solution())