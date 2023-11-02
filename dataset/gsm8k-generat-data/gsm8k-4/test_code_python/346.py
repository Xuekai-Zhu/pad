def solution():
    """Lucille is painting her room. Two of her walls are 3 meters wide and 2 meters tall. The third wall is 5 meters wide and 2 meters tall. The final wall is 4 meters wide and 2 meters tall. If each can of paint covers 2 square meters, how many cans of paint does Lucille need?"""
    # Define the dimensions of each wall
    wall1_width = 3
    wall1_height = 2
    wall2_width = 3
    wall2_height = 2
    wall3_width = 5
    wall3_height = 2
    wall4_width = 4
    wall4_height = 2

    # Calculate the total area to be painted
    total_area = (wall1_width * wall1_height) + (wall2_width * wall2_height) + (wall3_width * wall3_height) + (wall4_width * wall4_height)

    # Calculate the number of cans of paint needed, rounding up to the nearest integer
    cans_needed = -(-total_area // 2)

    result = cans_needed
    return result

print(solution())