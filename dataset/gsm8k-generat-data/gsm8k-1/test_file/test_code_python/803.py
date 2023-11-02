def solution():
    """Milo is making a mosaic with chips of glass. It takes twelve glass chips to make every square inch of the mosaic. A bag of glass chips holds 72 chips. Milo wants his mosaic to be three inches tall. If he has two bags of glass chips, how many inches long can he make his mosaic?"""
    chips_per_inch = 12
    chips_per_bag = 72
    total_chips = chips_per_bag * 2
    height = 3
    length = total_chips // (chips_per_inch * height)
    result = length
    return result

print(solution())