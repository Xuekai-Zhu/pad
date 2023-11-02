def solution():
    """Benny threw bologna at his balloons. He threw two pieces of bologna at each red balloon and three pieces of bologna at each yellow balloon. If Benny threw 58 pieces of bologna at a bundle of red and yellow balloons, and twenty of the balloons were red, then how many of the balloons in the bundle were yellow?"""

    red_balloons = 20
    bologna_per_red = 2
    bologna_per_yellow = 3
    total_bologna = 58

    # Calculate the total number of bologna pieces thrown at red balloons
    bologna_for_red = red_balloons * bologna_per_red

    # Calculate the total number of bologna pieces thrown at yellow balloons
    bologna_for_yellow = total_bologna - bologna_for_red

    # Calculate the total number of yellow balloons hit
    yellow_balloons = bologna_for_yellow // bologna_per_yellow

    result = yellow_balloons

    return result

print(solution())