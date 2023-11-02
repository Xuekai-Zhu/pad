def solution():
    """Cooper is building a brick fence around all four sides of his property. Each of the four walls of his fence is 20 bricks long, 5 bricks high, and 2 bricks deep. How many bricks does Cooper need to complete his fence?"""
    wall_length = 20
    wall_height = 5
    wall_depth = 2
    total_bricks = 4 * wall_length * wall_height * wall_depth
    result = total_bricks
    return result

print(solution())