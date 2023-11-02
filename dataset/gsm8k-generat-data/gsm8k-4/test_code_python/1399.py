def solution():
    """Austin is a surfer. He took a trip to the beach during surfing season and the highest wave he caught was two feet higher than four times his height. The shortest wave he caught was four feet higher than his height. The shortest wave was three feet higher than his 7-foot surfboard is long. How tall was the highest wave Austin caught?"""
    # Define the length of Austin's surfboard
    surfboard_length = 7

    # Calculate Austin's height
    height = (surfboard_length + 3 + 4) / 2

    # Calculate the height of the highest wave
    highest_wave_height = 4 * height + 2

    # return the result
    result = highest_wave_height
    return result

print(solution())