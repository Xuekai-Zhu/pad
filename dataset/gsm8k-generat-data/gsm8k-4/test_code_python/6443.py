def solution():
    """It takes Omar 12 minutes to raise his kite 240 feet into the air. Jasper can raise his kite at three times the rate of speed as Omar can raise his kite. If Jasper raises his kite to a height of 600 feet, how many minutes will it take?"""
    # Define Omar's variables
    omar_height = 240
    omar_time = 12
    
    # Define Jasper's variables
    jasper_height = 600
    jasper_speed = 3 * omar_height / omar_time
    
    # Calculate Jasper's time to raise his kite to the same height as Omar's
    jasper_time = jasper_height / (3 * omar_height) * omar_time
    
    result = jasper_time
    return result

print(solution())