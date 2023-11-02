def solution():
    # Calculate the total number of cherries needed for 9 quarts of syrup
    total_cherries = 500 * 9

    # Calculate the total time it takes Jerry to pick the needed amount of cherries
    cherry_picking_time = (total_cherries/300) * 2  # it takes Jerry 2 hours to pick 300 cherries

    # Calculate the total time it takes Jerry to make the syrup
    syrup_making_time = 3 * 9  # it takes Jerry 3 hours to make one quart of syrup

    # Calculate the total time it takes Jerry to make 9 quarts of syrup
    total_time = cherry_picking_time + syrup_making_time

    result = total_time
    return result

print(solution())