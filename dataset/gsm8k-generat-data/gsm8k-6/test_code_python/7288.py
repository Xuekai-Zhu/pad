def solution():
    # Calculate the distance traveled across the length of the lake
    distance_length = 10 * 2  # distance = speed x time

    # Calculate the speed in miles per minute
    speed = 10 / 60  # 10 MPH = (10/60) miles per minute

    # Calculate the distance traveled across the width of the lake
    distance_width = speed * 30  # distance = speed x time

    # Calculate the area of the lake in square miles
    area = distance_length * distance_width
    result = area
    return result

print(solution())