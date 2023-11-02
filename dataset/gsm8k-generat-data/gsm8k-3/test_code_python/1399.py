def solution():
    """Austin is a surfer. He took a trip to the beach during surfing season and the highest wave he caught was two feet higher than four times his height. The shortest wave he caught was four feet higher than his height. The shortest wave was three feet higher than his 7-foot surfboard is long. How tall was the highest wave Austin caught?"""
    # Define the height of Austin
    austin_height = (7 + 4) - 3

    # Calculate the height of the shortest wave
    shortest_wave_height = austin_height + 4

    # Calculate the height of the highest wave
    highest_wave_height = 4 * austin_height + 2

    # Display the height of the highest wave Austin caught
    result = highest_wave_height
    return result

print(solution())