def solution():
    """Mrs. Jackson has four boxes of Christmas decorations. There are 15 decorations in each box. She was only able to use 35 decorations and decided to give the rest to her neighbor. How many decorations did she give?"""
    # Define the number of boxes and decorations per box
    boxes = 4
    decorations_per_box = 15

    # Calculate the total number of decorations
    total_decorations = boxes * decorations_per_box

    # Calculate the number of decorations Mrs. Jackson didn't use
    unused_decorations = total_decorations - 35

    # return the result
    result = unused_decorations
    return result

print(solution())