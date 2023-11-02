def solution():
    """In one hour, Addison mountain's temperature will decrease to 3/4 of its temperature. If the current temperature of the mountain is 84 degrees, what will the temperature decrease by?"""
    current_temp = 84
    decrease_ratio = 3/4
    decrease_amount = current_temp * (1 - decrease_ratio)
    result = decrease_amount
    return result

print(solution())