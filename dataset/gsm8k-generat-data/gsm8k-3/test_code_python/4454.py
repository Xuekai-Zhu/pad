def solution():
    """James is building a hall of mirrors. Three of the walls will be completed covered with glass. If two of those walls are 30 feet by 12 feet and the third is 20 feet by 12 feet, how many square feet of glass does he need?"""
    # Calculate the area of the first two walls
    wall1_area = 30 * 12
    wall2_area = 30 * 12
    total_area1 = wall1_area + wall2_area

    # Calculate the area of the third wall
    wall3_area = 20 * 12

    # Calculate the total area of glass needed
    total_area = total_area1 + wall3_area

    # Display the total area
    result = total_area
    return result

print(solution())