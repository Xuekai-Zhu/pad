def solution():
    """A volcano erupts and spews ash into the sky. The ash cloud spreads out in a diameter eighteen times as far as the distance it shot up into the sky. If the ashes erupted three hundred feet into the sky, what was the radius of the ash cloud in feet?"""
    height = 300
    diameter = height * 18
    radius = diameter / 2
    result = radius
    return result

print(solution())