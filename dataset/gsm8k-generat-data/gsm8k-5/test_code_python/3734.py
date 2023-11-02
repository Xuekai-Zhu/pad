def solution():
    cherries_per_quart = 500
    cherries_needed = 9 * cherries_per_quart
    cherry_picking_time = 2  # in hours
    syrup_making_time = 3  # in hours

    # Calculate the total time needed to pick the required amount of cherries
    total_cherry_picking_time = (cherries_needed / 300) * cherry_picking_time

    # Calculate the total time needed to make the syrup
    total_syrup_making_time = 9 * syrup_making_time

    # Calculate the total time needed to make 9 quarts of syrup
    total_time = total_cherry_picking_time + total_syrup_making_time
    result = total_time
    return result

print(solution())