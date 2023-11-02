def solution():
    length = 100
    width = 50
    laps = 6

    # Calculate the distance around the perimeter of the rectangle
    perimeter = (2 * length) + (2 * width)

    # Calculate the distance each player will run (perimeter of rectangle times number of laps)
    distance = perimeter * laps
    result = distance
    return result

print(solution())