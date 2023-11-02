def solution():
    current_cups = 15
    increase_percent = 0.4

    # Calculate the increase in cups of water Happy needs to take
    increase_cups = current_cups * increase_percent

    # Calculate the recommended number of cups of water per week
    recommended_cups = current_cups + increase_cups
    result = recommended_cups
    return result

print(solution())