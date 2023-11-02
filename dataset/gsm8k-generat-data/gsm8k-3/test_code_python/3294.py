def solution():
    """Happy Cattle Ranch is home to 200 cows. Every year, the mother cows have enough calves that the number of cows the rancher owns rises by half the number of cows living on the ranch. If the rancher does not buy or sell any cows, how many cows will the rancher own on Happy Cattle Ranch in two years?"""
    # Define the initial number of cows on the ranch
    initial_cows = 200

    # Calculate the number of cows after one year
    cows_after_one_year = initial_cows + (0.5 * initial_cows)

    # Calculate the number of cows after two years
    cows_after_two_years = cows_after_one_year + (0.5 * cows_after_one_year)

    # Display the number of cows after two years
    result = cows_after_two_years
    return result

print(solution())