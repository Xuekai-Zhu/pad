def solution():
    """To increase her water intake to the recommended level by her doctor, Happy has to take 40% more cups of water than she takes now. If she is currently drinking 15 cups of water every week, what's the recommended number of cups per week?"""
    # Define the current number of cups of water Happy drinks
    current_cups = 15

    # Calculate the recommended increase in cups
    increase = current_cups * 0.4

    # Calculate the recommended number of cups per week
    recommended_cups = current_cups + increase

    # return the result
    result = recommended_cups
    return result

print(solution())