def solution():
    """Tom and his friends were filling up water balloons. Tom filled up 3 times as many water balloons as Luke. Luke filled up one fourth as many balloons as Anthony. If Anthony filled up 44 water balloons, how many did Tom fill up?"""
    # Define the number of water balloons filled up by Anthony
    anthony_balloons = 44

    # Calculate the number of water balloons filled up by Luke
    luke_balloons = anthony_balloons / 4

    # Calculate the number of water balloons filled up by Tom
    tom_balloons = luke_balloons * 3

    # Return the result
    result = tom_balloons
    return result

print(solution())