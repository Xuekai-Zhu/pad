def solution():
    """Annie has 6 barrettes, twice as many scrunchies as barrettes, and three fewer bobby pins than barrettes. What percentage of her hair decorations are bobby pins, rounded to the nearest percent?"""
    # Define the number of barrettes, scrunchies, and bobby pins
    barrettes = 6
    scrunchies = barrettes * 2
    bobby_pins = barrettes - 3

    # Calculate the total number of hair decorations
    total_decorations = barrettes + scrunchies + bobby_pins

    # Calculate the percentage of hair decorations that are bobby pins
    bobby_pin_percentage = (bobby_pins / total_decorations) * 100

    # Round the percentage to the nearest whole number
    rounded_percentage = round(bobby_pin_percentage)

    # Display the percentage of hair decorations that are bobby pins
    result = rounded_percentage
    return result

print(solution())