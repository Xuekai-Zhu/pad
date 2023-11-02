def solution():
    """Max fills up water balloons for 30 minutes at a rate of 2 water balloons every minute. Max’s friend Zach fills up water balloons for 40 minutes at a rate of 3 water balloons every minute. In the process, 10 of the water balloons pop on the ground. How many filled water balloons do Max and Zach have in total?"""
    # Calculate the number of water balloons filled by Max
    max_balloons = 30 * 2

    # Calculate the number of water balloons filled by Zach
    zach_balloons = 40 * 3

    # Subtract the number of balloons that popped
    total_balloons = max_balloons + zach_balloons - 10

    # return the result
    result = total_balloons
    return result

print(solution())