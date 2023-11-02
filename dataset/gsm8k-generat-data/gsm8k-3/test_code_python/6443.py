def solution():
    """It takes Omar 12 minutes to raise his kite 240 feet into the air. Jasper can raise his kite at three times the rate of speed as Omar can raise his kite. If Jasper raises his kite to a height of 600 feet, how many minutes will it take?"""
    # Omar's rate of raising his kite
    omar_rate = 240 / 12 # rate = distance / time

    # Jasper's rate of raising his kite
    jasper_rate = omar_rate * 3

    # Time it takes for Jasper to raise his kite to a height of 600 feet
    jasper_time = 600 / jasper_rate

    # Display the time it takes for Jasper to raise his kite
    result = jasper_time
    return result

print(solution())