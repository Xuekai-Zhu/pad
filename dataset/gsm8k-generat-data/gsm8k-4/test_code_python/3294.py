def solution():
    """Happy Cattle Ranch is home to 200 cows. Every year, the mother cows have enough calves that the number of cows the rancher owns rises by half the number of cows living on the ranch. If the rancher does not buy or sell any cows, how many cows will the rancher own on Happy Cattle Ranch in two years?"""
    # Define the initial number of cows
    initial_cows = 200

    # Calculate the number of cows after the first year
    first_year_cows = initial_cows + (initial_cows / 2)

    # Calculate the number of cows after the second year
    second_year_cows = first_year_cows + (first_year_cows / 2)

    result = second_year_cows
    return result

print(solution())