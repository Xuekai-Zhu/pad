def solution():
    """Mr. Curtis has 325 chickens on his farm where 28 are roosters and the rest are hens. Twenty hens do not lay eggs while the rest of the hens do. How many egg-laying hens does Mr. Curtis have on his farm?"""
    # Define the number of roosters
    roosters = 28

    # Define the total number of hens
    total_hens = 325 - roosters

    # Calculate the number of hens that do not lay eggs
    non_laying_hens = 20

    # Calculate the number of egg-laying hens
    laying_hens = total_hens - non_laying_hens

    # Return the result
    result = laying_hens
    return result

print(solution())