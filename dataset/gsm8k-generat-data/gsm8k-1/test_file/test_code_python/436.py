def solution():
    """The area of Billie's rectangular bedroom is 360 square feet. If the length of his room is 3 yards, what is the perimeter of the room in feet?"""
    area = 360
    length = 3*3   # 1 yard = 3 feet
    width = area/length
    perimeter = 2*(length+width)
    result = perimeter
    return result

print(solution())