def solution():
    """Tony tries to drink more water, so he has been tracking how much water he drinks. Yesterday, he drank 48 ounces of water, which is 4% less than what he drank two days ago. How much water did Tony drink two days ago?"""
    percent_decrease = 4
    yesterday_water = 48
    x = yesterday_water / (1 - (percent_decrease / 100))
    two_days_ago_water = x
    result = two_days_ago_water
    return result

print(solution())