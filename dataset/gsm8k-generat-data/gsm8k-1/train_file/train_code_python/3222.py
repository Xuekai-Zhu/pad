def solution():
    """There are chickens roaming the chicken farm. The roosters outnumber the hens 2 to 1. If there are 9,000 chickens on the chicken farm, how many roosters are there?"""
    total_chickens = 9000
    rooster_to_hen_ratio = 2/1
    roosters = total_chickens / (rooster_to_hen_ratio + 1) * rooster_to_hen_ratio
    result = roosters
    return result

print(solution())