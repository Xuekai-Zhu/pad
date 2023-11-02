def solution():
    """Will's breakfast supplied him 900 calories of energy. Then he decided to jog for half an hour, which used up 10 calories of energy per minute. What is Will's net calorie intake after jogging?"""
    # Define the initial calorie intake
    initial_calories = 900

    # Define the jogging time in minutes and the calories burned per minute
    jogging_time = 30
    calories_burned_per_minute = 10

    # Calculate the total calories burned during jogging
    total_calories_burned = jogging_time * calories_burned_per_minute

    # Calculate the net calorie intake
    net_calories = initial_calories - total_calories_burned

    # Display the net calorie intake
    result = net_calories
    return result

print(solution())