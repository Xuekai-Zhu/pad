def solution():
    """A boat is traveling across a square lake at 10 MPH. It takes 2 hours to go across the length of the lake. It then travels the whole width of the lake at the same speed, which takes 30 minutes. How many square miles is the lake?"""
    speed = 10  # MPH
    time_length = 2  # hours
    distance_length = speed * time_length  # miles

    time_width = 0.5  # hours (30 minutes)
    distance_width = speed * time_width  # miles

    # Since the lake is square, its area is equal to the length of one side squared
    # The distance length and width form the two sides of a right triangle, whose hypotenuse is equal to the side of the square lake
    hypotenuse = ((distance_length ** 2) + (distance_width ** 2)) ** 0.5
    area = hypotenuse ** 2
    result = area
    return result

print(solution())