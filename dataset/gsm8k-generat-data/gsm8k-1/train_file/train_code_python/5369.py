def solution():
    """If a circle has a radius of 14 feet, how many 6-inch pencils can be placed end-to-end across the diameter of the circle?"""
    radius = 14
    diameter = radius * 2
    pencil_length = 0.5 #in feet
    pencils_across = diameter / pencil_length
    result = int(pencils_across)
    return result

print(solution())