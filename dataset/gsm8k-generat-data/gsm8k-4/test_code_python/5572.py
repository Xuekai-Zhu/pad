def solution():
    """Alicia had a wonderful birthday party where she got lots of presents. 10 of the presents were in small boxes. 12 of the presents were in medium boxes. A third of all the presents she is given are in large boxes. How many presents did Alicia get for her birthday?"""
    # Define the number of presents in small boxes and medium boxes
    small_boxes = 10
    medium_boxes = 12

    # Calculate the total number of presents in small and medium boxes
    total_boxes = small_boxes + medium_boxes

    # Calculate the number of presents in large boxes
    large_boxes = round((total_boxes / 2), 0)

    # Calculate the total number of presents
    total_presents = small_boxes + medium_boxes + large_boxes

    # return the result
    result = total_presents
    return result

print(solution())