def solution():
    total_chickens = 100
    bcm_percent = 0.2
    bcm_hen_percent = 0.8

    # Calculate the total number of Black Copper Marans
    total_bcm = total_chickens * bcm_percent

    # Calculate the total number of Black Copper Marans hens
    total_bcm_hens = total_bcm * bcm_hen_percent
    result = total_bcm_hens
    return result

print(solution())