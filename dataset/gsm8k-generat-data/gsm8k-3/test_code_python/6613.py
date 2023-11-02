def solution():
    """Mr. Curtis has 325 chickens on his farm where 28 are roosters and the rest are hens. 
    Twenty hens do not lay eggs while the rest of the hens do. 
    How many egg-laying hens does Mr. Curtis have on his farm?"""
    
    # Calculate the number of hens
    hens = 325 - 28  # Subtract the number of roosters

    # Subtract the number of hens that do not lay eggs
    egg_laying_hens = hens - 20

    # Display the number of egg-laying hens
    result = egg_laying_hens
    return result

print(solution())