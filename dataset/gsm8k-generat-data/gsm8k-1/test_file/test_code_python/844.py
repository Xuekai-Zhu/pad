def solution():
    """A clothing store has 40 white shirts and 50 floral shirts. Half of the white shirts have collars, and 20 of the floral shirts have buttons. How many more floral shirts with no buttons are there than white shirts with no collars?"""
    num_white_shirts = 40
    num_floral_shirts = 50
    white_shirts_with_collars = num_white_shirts / 2
    floral_shirts_with_buttons = 20
    white_shirts_without_collars = num_white_shirts - white_shirts_with_collars
    floral_shirts_without_buttons = num_floral_shirts - floral_shirts_with_buttons
    difference = floral_shirts_without_buttons - white_shirts_without_collars
    result = difference
    return result

print(solution())