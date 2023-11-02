def solution():
    """Bill is a painter who is hired to paint a client’s house. The house has three bedrooms, and twice as many other rooms as bedrooms. The client wants each bedroom painted a different color, and the other rooms painted white. Each room takes 2 gallons of paint. Color paint comes in 1-gallon paint cans, and white paint comes in 3-gallon cans. How many cans of paint will Bill need for the whole house?"""
    num_bedrooms = 3
    num_other_rooms = num_bedrooms * 2
    num_rooms = num_bedrooms + num_other_rooms
    gallons_per_room = 2
    gallons_per_color_can = 1
    gallons_per_white_can = 3
    num_color_cans = num_bedrooms
    num_white_cans = (num_rooms - num_bedrooms) * gallons_per_room // gallons_per_white_can + \
                     (num_rooms - num_bedrooms) * gallons_per_room % gallons_per_white_can // gallons_per_color_can
    total_cans = num_color_cans + num_white_cans
    result = total_cans
    return result

print(solution())