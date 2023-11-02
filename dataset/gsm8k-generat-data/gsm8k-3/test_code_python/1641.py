def solution():
    """John uses the bathroom every 50 minutes. How many times does he use the bathroom during a 2.5-hour movie?"""
    # define the length of the movie in minutes
    length = 2.5 * 60

    # calculate the number of times John uses the bathroom
    bathroom_breaks = length // 50   # '//' is used to get the integer division

    # display the number of times John uses the bathroom
    result = bathroom_breaks
    return result

print(solution())