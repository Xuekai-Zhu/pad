def solution():
    """Tony tries to drink more water, so he has been tracking how much water he drinks. Yesterday, he drank 48 ounces of water, which is 4% less than what he drank two days ago. How much water did Tony drink two days ago?"""
    
    # Define the percentage decrease and the amount of water he drank yesterday
    PERCENT_DECREASE = 4
    YESTERDAY_WATER = 48

    # Calculate the total amount of water he drank 2 days ago
    water_2_days_ago = YESTERDAY_WATER / (1 - PERCENT_DECREASE/100)

    # Display the total amount of water he drank 2 days ago
    result = water_2_days_ago
    return result

print(solution())