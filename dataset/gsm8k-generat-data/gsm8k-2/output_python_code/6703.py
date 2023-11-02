def solution():
    """John starts climbing a very steep hill. He travels 1 foot vertically for every two feet horizontally. His elevation increases from 100 feet to 1450 feet. How far does he move horizontally, in feet?"""
    vertical_distance = 1450 - 100
    horizontal_distance = vertical_distance * 2
    result = horizontal_distance
    return result

print(solution())