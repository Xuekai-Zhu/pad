def solution():
    """In one hour, Addison mountain's temperature will decrease to 3/4  of its temperature. If the current temperature of the mountain is 84 degrees, what will the temperature decrease by?"""
    # Define the current temperature and the fraction by which it will decrease in one hour
    current_temp = 84
    decrease_fraction = 3/4

    # Calculate the temperature decrease in one hour
    decrease = current_temp * decrease_fraction

    # Display the temperature decrease
    result = decrease
    return result

print(solution())