def solution():
    """The temperature was 2 degrees Celsius. It dropped 8 degrees Celsius overnight and then increased 3 degrees Celsius in the morning. What was the temperature, in degrees Celsius, in the morning?"""
    initial_temp = 2
    temp_drop = 8
    temp_increase = 3
    final_temp = initial_temp - temp_drop + temp_increase
    result = final_temp
    return result

print(solution())