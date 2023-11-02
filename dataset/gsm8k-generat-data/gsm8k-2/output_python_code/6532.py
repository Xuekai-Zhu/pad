def solution():
    """Tony tries to drink more water, so he has been tracking how much water he drinks. Yesterday, he drank 48 ounces of water, which is 4% less than what he drank two days ago. How much water did Tony drink two days ago?"""
    yesterday_drinks = 48
    decrease_percentage = 4
    two_days_ago_drinks = yesterday_drinks / (1 - decrease_percentage / 100)
    result = two_days_ago_drinks
    return result

print(solution())