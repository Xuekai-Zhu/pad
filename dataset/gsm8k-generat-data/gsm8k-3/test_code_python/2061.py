def solution():
    """The coach of a football team asked his players to do six laps of the field. The field is in the shape of a rectangle of length 100 m and width 50 m. What is the distance each player will run, in meters?"""
    # Calculate the perimeter of the rectangle
    perimeter = 2 * (100 + 50)

    # Calculate the distance for each lap
    lap_distance = perimeter

    # Calculate the total distance for six laps
    total_distance = 6 * lap_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())