def solution():
    # Define the proportions of nickel and copper in 2020 nickels
    nickel_proportion = 0.25
    copper_proportion = 0.75
    # Check if nickel is the dominant material
    if nickel_proportion > copper_proportion:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())