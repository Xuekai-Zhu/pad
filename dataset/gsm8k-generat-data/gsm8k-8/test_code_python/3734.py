def solution():
    # Calculate the total number of cherries needed for 9 quarts of syrup
    total_cherries = 9 * 500

    # Calculate the total time it takes to pick the cherries
    cherry_picking_time = (total_cherries / 300) * 2

    # Calculate the total time it takes to make the syrup
    syrup_making_time = 3 * 9

    # Calculate the total time to make 9 quarts of syrup
    total_time = cherry_picking_time + syrup_making_time
    result = total_time
    return result

print(solution())