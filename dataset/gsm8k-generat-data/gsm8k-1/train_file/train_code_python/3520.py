def solution():
    """Will's breakfast supplied him 900 calories of energy. Then he decided to jog for half an hour, which used up 10 calories of energy per minute. What is Will's net calorie intake after jogging?"""
    breakfast_calories = 900
    jogging_time = 30 # in minutes
    jogging_calories = 10 * jogging_time
    net_calories = breakfast_calories - jogging_calories
    result = net_calories
    return result

print(solution())