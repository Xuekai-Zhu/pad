def solution():
    """Blinky wants to make a three-layer birthday cake for her mom. The recipe for the smallest layer of the cake requires 2 cups of sugar. 
    If the second layer is twice as big as the first and the third layer is three times larger than the second, 
    how many total cups of sugar will she need for the third layer?"""
    sugar_first_layer = 2
    sugar_second_layer = 2 * sugar_first_layer
    sugar_third_layer = 3 * sugar_second_layer
    total_sugar = sugar_third_layer
    result = total_sugar
    return result

print(solution())