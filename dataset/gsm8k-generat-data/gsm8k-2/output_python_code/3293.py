def solution():
    """Happy Cattle Ranch is home to 200 cows. Every year, the mother cows have enough calves that the number of cows the rancher owns rises by half the number of cows living on the ranch. If the rancher does not buy or sell any cows, how many cows will the rancher own on Happy Cattle Ranch in two years?"""
    starting_cows = 200
    first_year_cows = starting_cows + (starting_cows / 2)
    final_cows = first_year_cows + (first_year_cows / 2)
    result = final_cows
    return result

print(solution())