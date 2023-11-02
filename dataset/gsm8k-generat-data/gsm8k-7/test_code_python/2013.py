def solution():
    total_crayons = 120
    new_crayons = total_crayons / 3
    broken_crayons = total_crayons * 0.2

    # Calculate the number of slightly used crayons
    slightly_used_crayons = total_crayons - new_crayons - broken_crayons

    result = slightly_used_crayons
    return result

print(solution())