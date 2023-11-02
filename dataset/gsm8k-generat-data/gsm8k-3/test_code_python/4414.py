def solution():
    """John climbs up 3 flights of stairs.  Each flight is 10 feet.  He then climbs a rope that is half that height.  Finally, he climbs a ladder that is 10 feet longer than the rope.  How high up did he go?"""
    # Calculate the height of 3 flights of stairs
    stair_height = 3 * 10

    # Calculate the height of the rope
    rope_height = stair_height / 2

    # Calculate the height of the ladder
    ladder_height = rope_height + 10

    # Calculate the total height John climbed
    total_height = stair_height + rope_height + ladder_height

    # Display the total height
    result = total_height
    return result

print(solution())