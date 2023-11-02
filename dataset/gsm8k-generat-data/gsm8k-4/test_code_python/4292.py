def solution():
    """Jordan and Perry took a boat out to the lake to go fishing on a Monday morning. Jordan caught 4 fish and Perry caught double what Jordan caught. On the way back to shore, the boat tipped over and they lost one-fourth of their total catch. How many fish remain?"""
    # Define the number of fish Jordan caught
    jordan_fish = 4

    # Define the number of fish Perry caught
    perry_fish = jordan_fish * 2

    # Calculate the total catch before the boat tipped over
    total_catch = jordan_fish + perry_fish

    # Calculate the number of fish lost when the boat tipped over
    lost_fish = total_catch * 0.25

    # Calculate the number of fish that remain
    remaining_fish = total_catch - lost_fish

    result = remaining_fish
    return result

print(solution())