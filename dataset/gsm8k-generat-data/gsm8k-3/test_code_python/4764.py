def solution():
    """To increase her water intake to the recommended level by her doctor, Happy has to take 40% more cups of water than she takes now. If she is currently drinking 15 cups of water every week, what's the recommended number of cups per week?"""
    # Define the current cups of water and the percentage increase
    current_cups = 15
    increase_percent = 40

    # Calculate the recommended cups of water
    recommended_cups = current_cups + (current_cups * increase_percent / 100)

    # Display the recommended cups of water
    result = recommended_cups
    return result

print(solution())