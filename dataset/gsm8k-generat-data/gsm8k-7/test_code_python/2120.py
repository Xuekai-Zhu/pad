def solution():
    patrick_pins_round1 = 70
    richard_pins_round1 = patrick_pins_round1 + 15
    richard_pins_round2 = patrick_pins_round1 / 2 - 3

    patrick_total_pins = patrick_pins_round1 + richard_pins_round2
    richard_total_pins = richard_pins_round1 + richard_pins_round2
    difference = richard_total_pins - patrick_total_pins

    result = difference
    return result

print(solution())