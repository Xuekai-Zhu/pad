def solution():
    """Bill is a painter who is hired to paint a client’s house. The house has three bedrooms, and twice as many other rooms as bedrooms. The client wants each bedroom painted a different color, and the other rooms painted white. Each room takes 2 gallons of paint. Color paint comes in 1-gallon paint cans, and white paint comes in 3-gallon cans. How many cans of paint will Bill need for the whole house?"""
    # Define the number of bedrooms and other rooms
    bedrooms = 3
    other_rooms = bedrooms * 2

    # Calculate the total number of rooms
    total_rooms = bedrooms + other_rooms

    # Calculate the number of gallons of paint needed for the colored rooms
    colored_rooms_paint = 2 * bedrooms

    # Calculate the number of gallons of paint needed for the white rooms
    white_rooms_paint = 2 * other_rooms

    # Calculate the total number of gallons of paint needed
    total_paint = colored_rooms_paint + white_rooms_paint

    # Calculate the number of 1-gallon cans of colored paint needed
    colored_cans = colored_rooms_paint // 1
    if colored_rooms_paint % 1 != 0:
        colored_cans += 1

    # Calculate the number of 3-gallon cans of white paint needed
    white_cans = white_rooms_paint // 3
    if white_rooms_paint % 3 != 0:
        white_cans += 1

    # Calculate the total number of cans of paint needed
    total_cans = colored_cans + white_cans

    # return the result
    result = total_cans
    return result

print(solution())