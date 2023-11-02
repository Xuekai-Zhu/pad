def solution():
    """Mrs. Jackson has four boxes of Christmas decorations. There are 15 decorations in each box. She was only able to use 35 decorations and decided to give the rest to her neighbor. How many decorations did she give?"""
    boxes = 4
    decorations_per_box = 15
    total_decorations = boxes * decorations_per_box
    decorations_used = 35
    decorations_given = total_decorations - decorations_used
    result = decorations_given
    return result

print(solution())