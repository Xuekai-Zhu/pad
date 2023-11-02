def solution():
    total_chickens = 100
    percent_BCM = 20
    percent_BCM_hens = 80
    total_BCM = total_chickens * (percent_BCM / 100)
    total_BCM_hens = total_BCM * (percent_BCM_hens / 100)
    result = total_BCM_hens
    return result

print(solution())