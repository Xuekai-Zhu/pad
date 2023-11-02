def solution():
    """Hannah hangs a 2 foot by 4 foot painting on a 5 foot by 10 foot wall. What percentage of the wall is taken up by the painting?"""
    # Define the dimensions of the painting and the wall
    painting_width = 2
    painting_height = 4
    wall_width = 5
    wall_height = 10

    # Calculate the area of the painting and the area of the wall
    painting_area = painting_width * painting_height
    wall_area = wall_width * wall_height

    # Calculate the percentage of the wall taken up by the painting
    percentage = (painting_area / wall_area) * 100

    # return the result
    result = percentage
    return result

print(solution())