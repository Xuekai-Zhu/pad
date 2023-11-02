def solution():
    """Mrs. Jackson has four boxes of Christmas decorations. There are 15 decorations in each box. She was only able to use 35 decorations and decided to give the rest to her neighbor. How many decorations did she give?"""
    total_decorations = 4 * 15
    used_decorations = 35
    given_decorations = total_decorations - used_decorations
    result = given_decorations
    return result

print(solution())