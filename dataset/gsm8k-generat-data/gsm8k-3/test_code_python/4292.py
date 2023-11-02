def solution():
    """Jordan and Perry took a boat out to the lake to go fishing on a Monday morning. Jordan caught 4 fish and Perry caught double what Jordan caught. On the way back to shore, the boat tipped over and they lost one-fourth of their total catch. How many fish remain?"""
    # Calculate the number of fish Perry caught
    perry_catch = 4 * 2

    # Calculate the total catch before losing any fish
    total_catch = 4 + perry_catch

    # Calculate the number of fish lost when the boat tipped over
    lost_fish = total_catch * 0.25

    # Calculate the number of fish remaining
    remaining_fish = total_catch - lost_fish

    # Display the number of fish remaining
    result = remaining_fish
    return result

print(solution())