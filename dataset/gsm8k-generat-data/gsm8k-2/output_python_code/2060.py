def solution():
    """The coach of a football team asked his players to do six laps of the field. The field is in the shape of a rectangle of length 100 m and width 50 m. What is the distance each player will run, in meters?"""
    length = 100
    width = 50
    laps = 6
    distance = 2 * length + 2 * width
    total_distance = laps * distance
    result = total_distance
    return result

print(solution())