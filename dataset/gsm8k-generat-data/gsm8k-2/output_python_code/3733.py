def solution():
    """Jerry is making cherry syrup. He needs 500 cherries per quart of syrup. It takes him 2 hours to pick 300 cherries and 3 hours to make the syrup. How long will it take him to make 9 quarts of syrup?"""
    cherries_per_quart = 500
    cherries_for_9_quarts = cherries_per_quart * 9
    cherry_picking_time = 2
    syrup_making_time = 3
    total_time = cherry_picking_time + syrup_making_time
    cherry_picking_time_for_9_quarts = (cherries_for_9_quarts / 300) * cherry_picking_time
    total_time_for_9_quarts = total_time + cherry_picking_time_for_9_quarts
    result = total_time_for_9_quarts
    return result

print(solution())