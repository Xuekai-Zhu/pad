def solution():
    length = 100  # The length of the field is 100 meters
    width = 50  # The width of the field is 50 meters
    laps = 6  # The coach asked the players to do 6 laps

    # Calculate the distance each player will run
    distance_per_lap = 2 * length + 2 * width  # The distance of one lap is the perimeter of the rectangle
    total_distance = distance_per_lap * laps  # The total distance is the distance of one lap multiplied by the number of laps

    result = total_distance
    return result

print(solution())