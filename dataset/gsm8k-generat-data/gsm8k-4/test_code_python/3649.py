def solution():
    """Uncle Ben has 440 chickens on his farm. 39 are roosters and the rest are hens. 15 of his hens do not lay eggs, and the rest do. If each egg-laying hen lays 3 eggs, how many eggs will Uncle Ben have?"""
    # Define the total number of chickens and the number of roosters
    total_chickens = 440
    roosters = 39

    # Calculate the number of hens
    hens = total_chickens - roosters

    # Calculate the number of egg-laying hens
    laying_hens = hens - 15

    # Calculate the total number of eggs
    total_eggs = laying_hens * 3

    # return the result
    result = total_eggs
    return result

print(solution())