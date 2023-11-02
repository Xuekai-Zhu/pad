def solution():
    """Will's breakfast supplied him 900 calories of energy. Then he decided to jog for half an hour, which used up 10 calories of energy per minute. What is Will's net calorie intake after jogging?"""
    # Define the initial calorie intake from breakfast
    calorie_intake = 900

    # Define the calorie burn from jogging
    calorie_burn = 10 * 30

    # Calculate the net calorie intake
    net_calorie_intake = calorie_intake - calorie_burn

    # return the result
    result = net_calorie_intake
    return result

print(solution())