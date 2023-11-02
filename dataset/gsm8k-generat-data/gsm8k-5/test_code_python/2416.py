def solution():
    barrettes = 6  # Annie has 6 barrettes
    scrunchies = barrettes * 2  # Annie has twice as many scrunchies as barrettes
    bobby_pins = barrettes - 3  # Annie has three fewer bobby pins than barrettes

    total_decorations = barrettes + scrunchies + bobby_pins  # Calculate the total number of hair decorations

    # Calculate the percentage of hair decorations that are bobby pins
    bobby_pin_percent = (bobby_pins / total_decorations) * 100

    # Round the percentage to the nearest whole number
    rounded_percent = round(bobby_pin_percent)

    result = rounded_percent
    return result

print(solution())