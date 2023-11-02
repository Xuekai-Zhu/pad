def solution():
    """A boat is traveling across a square lake at 10 MPH. It takes 2 hours to go across the length of the lake. It then travels the whole width of the lake at the same speed, which takes 30 minutes. How many square miles is the lake?"""
    length_time = 2  # hours
    width_time = 0.5  # hours
    speed = 10  # miles per hour
    length = speed * length_time
    width = speed * width_time
    area = length * width
    result = area
    return result

print(solution())