def solution():
    """There are chickens roaming the chicken farm. The roosters outnumber the hens 2 to 1. If there are 9,000 chickens on the chicken farm, how many roosters are there?"""
    # Define the total number of chickens and the ratio of roosters to hens
    total_chickens = 9000
    rooster_to_hen_ratio = 2/1

    # Calculate the total number of roosters
    roosters = total_chickens / (rooster_to_hen_ratio + 1 + 2)

    # Return the result
    result = roosters
    return result

print(solution())