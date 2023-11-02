def solution():
    calories_consumed_jogging = 10 * 30  # Will used up 10 calories of energy per minute jogging for half an hour
    net_calories = 900 - calories_consumed_jogging  # Calculate the net calorie intake

    result = net_calories
    return result

print(solution())