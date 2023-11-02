def solution():
    """Of the 3 friends, Harry has 4 times as many fish as Joe, and Joe has 8 times as many fish as Sam does. If Sam has 7 fish, how many fish does Harry have?"""
    # Define the number of fish Sam has
    sam_fish = 7

    # Calculate the number of fish Joe has
    joe_fish = sam_fish * 8

    # Calculate the number of fish Harry has
    harry_fish = joe_fish * 4

    # Display the number of fish Harry has
    result = harry_fish
    return result

print(solution())