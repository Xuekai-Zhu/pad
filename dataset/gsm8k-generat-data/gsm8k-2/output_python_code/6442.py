def solution():
    """It takes Omar 12 minutes to raise his kite 240 feet into the air. Jasper can raise his kite at three times the rate of speed as Omar can raise his kite. If Jasper raises his kite to a height of 600 feet, how many minutes will it take?"""
    omar_speed = 240 / 12
    jasper_speed = 3 * omar_speed
    jasper_time = 600 / jasper_speed
    result = jasper_time
    return result

print(solution())