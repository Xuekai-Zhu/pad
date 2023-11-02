def solution():
    """Tommy has 13 items in his pencil case. The pens are twice as many as the pencils and there's one eraser. How many pencils are there?"""
    # Define the total number of items in the pencil case and the number of erasers
    total_items = 13
    erasers = 1

    # Calculate the number of pens
    pens = total_items - erasers
    pencils = pens / 2

    # Return the number of pencils
    result = pencils
    return result

print(solution())