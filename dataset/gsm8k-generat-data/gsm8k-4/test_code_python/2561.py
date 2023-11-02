def solution():
    """Happy Island has 60 turtles. This means there are 10 more than 2 times as many turtles on Happy Island as on Lonely Island. How many turtles are there on Lonely Island?"""
    # Define the number of turtles on Happy Island and the difference in turtles between the two islands
    happy_turtles = 60
    diff_turtles = 10

    # Calculate the number of turtles on Lonely Island using the given information
    lonely_turtles = (happy_turtles - diff_turtles) / 2

    # Return the result
    result = lonely_turtles
    return result

print(solution())