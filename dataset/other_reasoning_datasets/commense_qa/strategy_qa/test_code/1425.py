def solution():
    # Define the number of soldiers in one battalion and the circulation of The Atlantic
    soldiers_per_battalion = 1000
    atlantic_circulation = 478534
    # Calculate the number of soldiers needed for 500 battalions
    soldiers_needed = soldiers_per_battalion * 500
    # Check if the number of Atlantic readers is greater than or equal to the number of soldiers needed
    if atlantic_circulation >= soldiers_needed:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())