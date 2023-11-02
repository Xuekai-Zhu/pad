def solution():
    # Define Darcie's age and the ratios
    darcie_age = 4
    mother_to_darcie_ratio = 6
    father_to_mother_ratio = 5/4

    # Calculate the mother's age and the father's age
    mother_age = darcie_age * mother_to_darcie_ratio
    father_age = mother_age * father_to_mother_ratio

    # Return the father's age
    result = father_age
    return result

print(solution())