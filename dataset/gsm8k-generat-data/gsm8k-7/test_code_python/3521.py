def solution():
    breakfast_calories = 900
    jogging_time = 30 # in minutes
    jogging_calories_per_minute = 10

    # Calculate the total calories used up during jogging
    jogging_calories = jogging_time * jogging_calories_per_minute

    # Calculate the net calorie intake after jogging
    net_calories = breakfast_calories - jogging_calories
    result = net_calories
    return result

print(solution())