def solution():
    # Calculate the total number bricks Cooper needs for his fence
    length_of_wall = 20  # number of bricks in length of each wall
    height_of_wall = 5  # number of bricks in height of each wall
    depth_of_wall = 2  # number of bricks in depth of each wall
    total_bricks = 4 * length_of_wall * height_of_wall * depth_of_wall  # Cooper is building a fence around all four sides of his property
    result = total_bricks
    return result

print(solution())