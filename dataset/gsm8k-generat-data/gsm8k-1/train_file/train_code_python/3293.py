def solution():
    """Happy Cattle Ranch is home to 200 cows. Every year, the mother cows have enough calves that the number of cows the rancher owns rises by half the number of cows living on the ranch. If the rancher does not buy or sell any cows, how many cows will the rancher own on Happy Cattle Ranch in two years?"""
    initial_cows = 200
    years = 2
    total_cows = initial_cows * ((1 + 0.5) ** years)
    result = total_cows
    return result

print(solution())