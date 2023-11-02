def solution():
    """A park is 1000 feet long and 2000 feet wide. If there is 1 tree per 20 square feet, how many trees are there in the park?"""
    park_length = 1000
    park_width = 2000
    square_feet = park_length * park_width
    trees = square_feet / 20
    result = trees
    return result

print(solution())