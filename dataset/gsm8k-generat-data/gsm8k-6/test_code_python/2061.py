def solution():
    # Calculate the total distance around the field
    perimeter = 2 * (100 + 50)  # perimeter of rectangle is 2(length + width)

    # Calculate the distance each player will run
    distance_per_player = 6 * perimeter  # each player does 6 laps
    result = distance_per_player
    return result

print(solution())