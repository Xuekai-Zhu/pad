def solution():
    total_chickens = 100
    bcm_percent = 0.2
    bcm_count = bcm_percent * total_chickens
    bcm_hen_percent = 0.8
    bcm_hen_count = bcm_hen_percent * bcm_count
    result = bcm_hen_count
    return result

print(solution())