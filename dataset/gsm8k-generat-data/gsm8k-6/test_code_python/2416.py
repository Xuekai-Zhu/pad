def solution():
    barrettes = 6
    scrunchies = 2 * barrettes
    bobby_pins = barrettes - 3
    total_decorations = barrettes + scrunchies + bobby_pins
    percentage_bobby_pins = round((bobby_pins / total_decorations) * 100)
    result = percentage_bobby_pins
    return result

print(solution())