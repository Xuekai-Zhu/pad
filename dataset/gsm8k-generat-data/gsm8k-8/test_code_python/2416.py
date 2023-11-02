def solution():
    barrettes = 6
    scrunchies = 2 * barrettes
    bobby_pins = barrettes - 3

    total_decorations = barrettes + scrunchies + bobby_pins
    bobby_pins_percent = round((bobby_pins / total_decorations) * 100)

    result = bobby_pins_percent
    return result

print(solution())