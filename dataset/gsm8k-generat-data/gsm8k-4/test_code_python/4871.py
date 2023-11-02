def solution():
    """Mrs. Fredrickson has 80 chickens where 1/4 are roosters and the rest are hens. Only three-fourths of those hens lay eggs. How many chickens does Mr. Fredrickson have that do not lay eggs?"""
    # Calculate the number of roosters
    roosters = 80 * 0.25

    # Calculate the number of hens
    hens = 80 - roosters

    # Calculate the number of hens that lay eggs
    laying_hens = hens * 0.75

    # Calculate the number of chickens that do not lay eggs
    non_laying_chickens = roosters + (hens - laying_hens)

    result = non_laying_chickens
    return result

print(solution())