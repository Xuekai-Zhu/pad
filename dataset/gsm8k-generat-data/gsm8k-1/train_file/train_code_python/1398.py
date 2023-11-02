def solution():
    """Austin is a surfer. He took a trip to the beach during surfing season and the highest wave he caught was two feet higher than four times his height. The shortest wave he caught was four feet higher than his height. The shortest wave was three feet higher than his 7-foot surfboard is long. How tall was the highest wave Austin caught?"""
    surfboard_length = 7
    shortest_wave = surfboard_length + 3
    height = shortest_wave - 4
    highest_wave = height * 4 + 2
    result = highest_wave
    return result

print(solution())