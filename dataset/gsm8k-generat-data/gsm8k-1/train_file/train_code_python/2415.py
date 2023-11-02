def solution():
    """Annie has 6 barrettes, twice as many scrunchies as barrettes, and three fewer bobby pins than barrettes.
    What percentage of her hair decorations are bobby pins, rounded to the nearest percent?"""
    barrettes = 6
    scrunchies = barrettes * 2
    bobby_pins = barrettes - 3
    total_hair_decorations = barrettes + scrunchies + bobby_pins
    percentage_bobby_pins = round((bobby_pins / total_hair_decorations) * 100)
    result = percentage_bobby_pins
    return result

print(solution())