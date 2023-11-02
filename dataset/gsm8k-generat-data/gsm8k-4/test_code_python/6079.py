def solution():
    """Erin put 16 curlers in her hair. One-fourth of the curlers are small pink ones. There are twice as many medium blue curlers as there are pink ones. The rest are large green curlers. How many large green curlers does Erin have in her hair?"""
    # Define the total number of curlers
    total_curlers = 16

    # Calculate the number of small pink curlers
    pink_curlers = total_curlers / 4

    # Calculate the number of medium blue curlers
    blue_curlers = pink_curlers * 2

    # Calculate the number of large green curlers
    green_curlers = total_curlers - pink_curlers - blue_curlers

    # return the result
    result = green_curlers
    return result

print(solution())