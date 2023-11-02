def solution():
    """Jerry is making cherry syrup. He needs 500 cherries per quart of syrup. It takes him 2 hours to pick 300 cherries and 3 hours to make the syrup. How long will it take him to make 9 quarts of syrup?"""
    # Define the amount of cherries and time it takes to make one quart of syrup
    cherries_per_quart = 500
    time_per_quart = 3

    # Calculate the time it takes to pick enough cherries for one quart of syrup
    time_to_pick_cherries = 2 * cherries_per_quart / 300

    # Calculate the total time it takes to make one quart of syrup
    total_time_per_quart = time_to_pick_cherries + time_per_quart

    # Calculate the total time it takes to make 9 quarts of syrup
    total_time = total_time_per_quart * 9

    # return the result
    result = total_time
    return result

print(solution())