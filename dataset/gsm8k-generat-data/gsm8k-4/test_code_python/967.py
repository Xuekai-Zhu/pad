def solution():
    """In one hour, Addison mountain's temperature will decrease to 3/4  of its temperature. If the current temperature of the mountain is 84 degrees, what will the temperature decrease by?"""
    # Define the current temperature of the mountain
    current_temp = 84

    # Calculate the temperature decrease after one hour
    decreased_temp = current_temp * (1 - 3/4)

    # return the result
    result = decreased_temp
    return result

print(solution())