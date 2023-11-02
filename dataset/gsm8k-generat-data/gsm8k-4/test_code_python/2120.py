def solution():
    """In the first round of bowling, Patrick knocked down a total of 70 pins and Richard knocked down 15 more pins than Patrick. In the second round, Patrick knocked down twice as many pins as Richard in the first round and Richard knocked down 3 less than Patrick. How many more pins in total did Richard knock down than Patrick?"""
    # Define the number of pins knocked down by Patrick in the first round
    patrick_pins_round_1 = 70

    # Define the number of pins knocked down by Richard in the first round
    richard_pins_round_1 = patrick_pins_round_1 + 15

    # Calculate the number of pins knocked down by Patrick in the second round
    patrick_pins_round_2 = 2 * (richard_pins_round_1 - 3)

    # Calculate the total number of pins knocked down by Patrick
    patrick_pins_total = patrick_pins_round_1 + patrick_pins_round_2

    # Calculate the total number of pins knocked down by Richard
    richard_pins_total = patrick_pins_round_1 + richard_pins_round_1 + (patrick_pins_round_2 - richard_pins_round_1)

    # Calculate the difference in the total number of pins knocked down by Richard and Patrick
    difference = richard_pins_total - patrick_pins_total

    # return the result
    result = difference
    return result

print(solution())