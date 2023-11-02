def solution():
    num_chickens = 100  # there are 100 chickens in total
    num_bcm = int(num_chickens * 0.2)  # 20% of chickens are BCM
    num_bcm_hens = int(num_bcm * 0.8)  # 80% of BCMs are hens

    result = num_bcm_hens
    return result

print(solution())