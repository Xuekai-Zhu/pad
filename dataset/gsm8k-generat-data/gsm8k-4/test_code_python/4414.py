def solution():
    """John climbs up 3 flights of stairs. Each flight is 10 feet. He then climbs a rope that is half that height. Finally, he climbs a ladder that is 10 feet longer than the rope. How high up did he go?"""
    # Define the height of one flight of stairs
    stairs_height = 10

    # Calculate the total height climbed by stairs
    stairs_total = stairs_height * 3

    # Calculate the height climbed by the rope
    rope_height = stairs_height / 2

    # Calculate the height of the ladder
    ladder_height = rope_height + 10

    # Calculate the total height climbed
    total_height = stairs_total + rope_height + ladder_height

    result = total_height
    return result

print(solution())