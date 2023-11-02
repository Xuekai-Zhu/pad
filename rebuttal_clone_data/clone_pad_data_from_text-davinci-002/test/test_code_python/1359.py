def solution():
     barrettes = 6
     scrunchies = 2 * barrettes
     bobby_pins = barrettes - 3
     total_hair_decorations = barrettes + scrunchies + bobby_pins
     bobby_pin_percentage = (bobby_pins / total_hair_decorations) * 100
     result = round(bobby_pin_percentage, 0)
     return result

print(solution())