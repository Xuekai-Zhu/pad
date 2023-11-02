def solution():
    """Annie has 6 barrettes, twice as many scrunchies as barrettes, and three fewer bobby pins than barrettes. What percentage of her hair decorations are bobby pins, rounded to the nearest percent?"""
    # Define the number of barrettes and calculate the number of scrunchies and bobby pins
    barrettes = 6
    scrunchies = barrettes * 2
    bobby_pins = barrettes - 3

    # Calculate the total number of hair decorations
    total_decorations = barrettes + scrunchies + bobby_pins

    # Calculate the percentage of decorations that are bobby pins
    bobby_pins_percentage = (bobby_pins / total_decorations) * 100

    # Round the percentage to the nearest integer
    bobby_pins_percentage = round(bobby_pins_percentage)

    # return the result
    result = bobby_pins_percentage
    return result

print(solution())