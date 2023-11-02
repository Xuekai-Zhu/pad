def solution():
    """The coach of a football team asked his players to do six laps of the field. The field is in the shape of a rectangle of length 100 m and width 50 m. What is the distance each player will run, in meters?"""
    # Define the dimensions of the field
    length = 100
    width = 50

    # Calculate the distance around the field
    perimeter = 2 * (length + width)

    # Calculate the distance each player will run for 6 laps
    distance_per_player = perimeter * 6

    # Return the result
    result = distance_per_player
    return result

print(solution())