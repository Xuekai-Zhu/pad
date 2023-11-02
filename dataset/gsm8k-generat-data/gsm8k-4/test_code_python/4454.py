def solution():
    """James is building a hall of mirrors. Three of the walls will be completed covered with glass. If two of those walls are 30 feet by 12 feet and the third is 20 feet by 12 feet, how many square feet of glass does he need?"""
    # Define the dimensions of the two larger walls
    large_wall_1_length = 30
    large_wall_1_height = 12
    large_wall_2_length = 30
    large_wall_2_height = 12

    # Define the dimensions of the smaller wall
    small_wall_length = 20
    small_wall_height = 12

    # Calculate the area of each wall
    large_wall_1_area = large_wall_1_length * large_wall_1_height
    large_wall_2_area = large_wall_2_length * large_wall_2_height
    small_wall_area = small_wall_length * small_wall_height

    # Calculate the total area of glass needed
    total_area = large_wall_1_area + large_wall_2_area + small_wall_area

    # return the result
    result = total_area
    return result

print(solution())