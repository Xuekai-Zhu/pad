def solution():
    # Calculate the number of calories used up during jogging
    calories_used_up = 10 * 30  # Will jogged for half an hour, so he used up 10 calories per minute

    # Calculate Will's net calorie intake after jogging
    net_calories = 900 - calories_used_up
    result = net_calories
    return result

print(solution())