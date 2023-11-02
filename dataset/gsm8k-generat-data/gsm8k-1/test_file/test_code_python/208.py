def solution():
    """Gary likes to walk around the edge of the local park, which is a rectangle that measures 1.5 miles by 6 miles. If he walks at 3 miles/hour, how many hours does he spend walking?"""
    length = 6
    width = 1.5
    perimeter = 2 * (length + width)
    speed = 3
    time = perimeter / speed
    result = time
    return result

print(solution())