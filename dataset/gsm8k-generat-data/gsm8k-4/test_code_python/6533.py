def solution():
    """Tony tries to drink more water, so he has been tracking how much water he drinks. Yesterday, he drank 48 ounces of water, which is 4% less than what he drank two days ago. How much water did Tony drink two days ago?"""
    # Calculate the percentage of water Tony drank two days ago
    percentage = 100 / 96

    # Calculate the amount of water Tony drank two days ago
    water_two_days_ago = 48 * percentage

    # return the result
    result = water_two_days_ago
    return result

print(solution())