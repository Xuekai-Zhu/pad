def solution():
    # Calculate the number of Black Copper Marans chickens
    BCM_chickens = 0.20 * 100  # 20 percent of 100 chickens are Black Copper Marans
    BCM_hens = 0.80 * BCM_chickens  # 80 percent of Black Copper Marans chickens are hens
    result = BCM_hens
    return result

print(solution())