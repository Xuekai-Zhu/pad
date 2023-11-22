def solution():
    
    # Define the number of crabs Bo has
    bo_crabs = 40

    # Calculate the number of crabs Monic has
    monic_crabs = bo_crabs - 4

    # Calculate the number of crabs Rani has
    rai_crabs = monic_crabs + 10

    # Calculate the total number of crabs the three have together
    total_crabs = bo_crabs + monic_crabs + rai_crabs

    # Display the total number of crabs
    result = total_crabs
    return result

print(solution())