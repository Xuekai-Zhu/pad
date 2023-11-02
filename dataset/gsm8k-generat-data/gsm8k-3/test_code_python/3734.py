def solution():
    """Jerry is making cherry syrup. He needs 500 cherries per quart of syrup. It takes him 2 hours to pick 300 cherries and 3 hours to make the syrup. How long will it take him to make 9 quarts of syrup?"""
    # Define the number of cherries needed per quart of syrup
    CHERRIES_PER_QUART = 500

    # Define the time it takes to pick a certain number of cherries
    CHERRY_PICKING_TIME = 2

    # Define the time it takes to make a quart of syrup
    SYRUP_MAKING_TIME = 3

    # Define the number of quarts of syrup needed
    QUARTS_OF_SYRUP = 9

    # Calculate the total number of cherries needed
    total_cherries = CHERRIES_PER_QUART * QUARTS_OF_SYRUP

    # Calculate the time it takes to pick the needed number of cherries
    cherry_picking_time = (total_cherries / 300) * CHERRY_PICKING_TIME

    # Calculate the total time it takes to make the syrup
    syrup_making_time = QUARTS_OF_SYRUP * SYRUP_MAKING_TIME

    # Calculate the total time needed to make the syrup
    total_time = cherry_picking_time + syrup_making_time

    # Display the total time needed
    result = total_time
    return result

print(solution())