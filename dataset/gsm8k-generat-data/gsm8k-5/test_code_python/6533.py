def solution():
    water_yesterday = 48  # Tony drank 48 ounces of water yesterday
    percent_less = 4  # Tony drank 4% less than two days ago

    # Calculate how much water Tony drank two days ago
    water_two_days_ago = water_yesterday / (1 - percent_less/100)
    result = water_two_days_ago
    return result

print(solution())