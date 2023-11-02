def solution():
    total_apples = 200  # Total number of apples in the orchard
    rotten_apples = 0.4 * total_apples  # Number of rotten apples
    smelling_rotten_apples = 0.7 * rotten_apples  # Number of rotten apples that smelled

    # Calculate the number of rotten apples that did not smell
    non_smelling_rotten_apples = rotten_apples - smelling_rotten_apples
    result = non_smelling_rotten_apples
    return result

print(solution())