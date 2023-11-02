def solution():
    
    barrettes = 6
    scrunchies = barrettes * 2
    bobby_pins = barrettes - 3
    total_hair_decorations = barrettes + scrunchies + bobby_pins
    percentage_bobby_pins = round((bobby_pins / total_hair_decorations) * 100)
    result = percentage_bobby_pins
    return result

print(solution())