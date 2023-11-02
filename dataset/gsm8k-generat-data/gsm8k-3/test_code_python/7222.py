def solution():
    """A farm has 100 chickens. 20 percent are Black Copper Marans, 
    and 80 percent of the Black Copper Marans are hens. How many BCM hens are there?"""
    
    # Calculate the number of BCM chickens on the farm
    bcm_chickens = 0.2 * 100

    # Calculate the number of BCM hens on the farm
    bcm_hens = 0.8 * bcm_chickens

    # Display the number of BCM hens on the farm
    result = bcm_hens
    return result

print(solution())