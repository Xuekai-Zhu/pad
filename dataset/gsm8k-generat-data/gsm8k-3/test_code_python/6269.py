def solution():
    """Tommy has 13 items in his pencil case. The pens are twice as many as the pencils and there's one eraser. How many pencils are there?"""
    # Define the number of erasers
    erasers = 1

    # Define the ratio of pens to pencils
    pen_pencil_ratio = 2

    # Calculate the number of pens
    pens = pen_pencil_ratio * (13 - erasers) / (1 + pen_pencil_ratio)

    # Calculate the number of pencils
    pencils = 13 - erasers - pens

    # Display the number of pencils
    result = pencils
    return result

print(solution())