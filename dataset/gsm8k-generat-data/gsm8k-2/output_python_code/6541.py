def solution():
    """Bill is a painter who is hired to paint a client’s house. The house has three bedrooms, and twice as many other rooms as bedrooms. The client wants each bedroom painted a different color, and the other rooms painted white. Each room takes 2 gallons of paint. Color paint comes in 1-gallon paint cans, and white paint comes in 3-gallon cans. How many cans of paint will Bill need for the whole house?"""
    bedrooms = 3
    other_rooms = bedrooms * 2
    total_rooms = bedrooms + other_rooms
    colored_rooms = bedrooms
    white_rooms = other_rooms
    gallons_needed = (colored_rooms * 2) + (white_rooms * 2)
    one_gallon_cans = colored_rooms
    three_gallon_cans = white_rooms + math.ceil(gallons_needed / 3)
    total_cans = one_gallon_cans + three_gallon_cans
    result = total_cans
    return result

print(solution())