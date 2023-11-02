def solution():
    """A farm has 100 chickens. 20 percent are Black Copper Marans, and 80 percent of the Black Copper Marans are hens. How many BCM hens are there?"""
    total_chickens = 100
    bcm_percent = 20
    bcm_count = total_chickens * (bcm_percent / 100)
    bcm_hen_percent = 80
    bcm_hen_count = bcm_count * (bcm_hen_percent / 100)
    result = bcm_hen_count
    return result

print(solution())