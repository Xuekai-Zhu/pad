def solution():
    """In one hour, Addison mountain's temperature will decrease to 3/4 of its temperature. If the current temperature of the mountain is 84 degrees, what will the temperature decrease by?"""
    initial_temp = 84
    decreased_temp = initial_temp * 3/4
    temp_decrease = initial_temp - decreased_temp
    result = temp_decrease
    return result

print(solution())