def solution():
    """Hannah hangs a 2 foot by 4 foot painting on a 5 foot by 10 foot wall. What percentage of the wall is taken up by the painting?"""
    # Define the dimensions of the painting and the wall
    painting_length = 2
    painting_width = 4
    wall_length = 5
    wall_width = 10

    # Calculate the area of the painting and the wall
    painting_area = painting_length * painting_width
    wall_area = wall_length * wall_width

    # Calculate the percentage of the wall taken up by the painting
    percentage = (painting_area / wall_area) * 100

    # Display the percentage
    result = percentage
    return result

print(solution())