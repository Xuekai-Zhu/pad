def solution():
    num_barrettes = 6
    num_scrunchies = num_barrettes * 2
    num_bobby_pins = num_barrettes - 3

    total_decorations = num_barrettes + num_scrunchies + num_bobby_pins

    # Calculate the percentage of decorations that are bobby pins
    bobby_pins_percent = (num_bobby_pins / total_decorations) * 100
    rounded_percent = round(bobby_pins_percent)

    result = rounded_percent
    return result

print(solution())