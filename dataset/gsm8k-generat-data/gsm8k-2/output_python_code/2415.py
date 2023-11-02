def solution():
    """Annie has 6 barrettes, twice as many scrunchies as barrettes, and three fewer bobby pins than barrettes. What percentage of her hair decorations are bobby pins, rounded to the nearest percent?"""
    barrettes = 6
    scrunchies = 2 * barrettes
    bobby_pins = barrettes - 3
    total_decorations = barrettes + scrunchies + bobby_pins
    bobby_pins_percentage = (bobby_pins / total_decorations) * 100
    result = round(bobby_pins_percentage)
    return result

print(solution())