def solution():
    """A farm has 100 chickens. 20 percent are Black Copper Marans, and 80 percent of the Black Copper Marans are hens. How many BCM hens are there?"""
    total_chickens = 100
    bcm_percentage = 0.2
    bcm_count = int(total_chickens * bcm_percentage)
    bcm_hen_percentage = 0.8
    bcm_hen_count = int(bcm_count * bcm_hen_percentage)
    result = bcm_hen_count
    return result

print(solution())