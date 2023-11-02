def solution():
    
    # Define the number of families Ali calls
    ali_families = 3

    # Define the number of families each family calls
    family_families = 3

    # Calculate the total number of families
    total_families = ali_families + (3 * family_families)

    # Display the total number of families
    result = total_families
    return result

print(solution())