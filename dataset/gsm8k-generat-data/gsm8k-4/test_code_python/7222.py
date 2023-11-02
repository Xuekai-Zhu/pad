def solution():
    """A farm has 100 chickens.  20 percent are Black Copper Marans, and 80 percent of the Black Copper Marans are hens.  How many BCM hens are there?"""
    # Define the total number of chickens
    total_chickens = 100

    # Calculate the number of Black Copper Marans chickens
    bcm_chickens = total_chickens * 0.2

    # Calculate the number of BCM hens
    bcm_hens = bcm_chickens * 0.8

    # return the result
    result = bcm_hens
    return result

print(solution())