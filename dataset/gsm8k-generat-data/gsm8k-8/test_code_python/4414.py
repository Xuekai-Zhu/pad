def solution():
    # Define the height of each flight of stairs
    flight_height = 10

    # Calculate the total height John climbed on the stairs
    stairs_climbed = flight_height * 3

    # Calculate the height of the rope John climbed
    rope_height = flight_height / 2

    # Calculate the height of the ladder John climbed
    ladder_height = rope_height + 10

    # Calculate the total height John climbed
    total_height = stairs_climbed + rope_height + ladder_height
    result = total_height
    return result

print(solution())