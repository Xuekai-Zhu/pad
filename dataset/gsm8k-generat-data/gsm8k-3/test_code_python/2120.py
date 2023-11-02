def solution():
    """In the first round of bowling, Patrick knocked down a total of 70 pins and Richard knocked down 15 more pins than Patrick. In the second round, Patrick knocked down twice as many pins as Richard in the first round and Richard knocked down 3 less than Patrick. How many more pins in total did Richard knock down than Patrick?"""
    
    # Calculate the number of pins knocked down by Richard in the first round
    patrick_pins = 70
    richard_pins = patrick_pins + 15

    # Calculate the number of pins knocked down by Patrick in the second round
    richard_pins_1 = richard_pins - 3
    patrick_pins_1 = 2 * richard_pins_1

    # Calculate the total number of pins knocked down by each player
    richard_total_pins = richard_pins + richard_pins_1
    patrick_total_pins = patrick_pins + patrick_pins_1

    # Calculate the difference in pins knocked down by Richard and Patrick
    difference = richard_total_pins - patrick_total_pins

    # Display the difference in pins knocked down
    result = difference
    return result

print(solution())