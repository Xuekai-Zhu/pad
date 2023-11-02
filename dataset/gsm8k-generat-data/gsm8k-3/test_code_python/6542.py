def solution():
    """Bill is a painter who is hired to paint a client’s house. The house has three bedrooms, and twice as many other rooms as bedrooms. The client wants each bedroom painted a different color, and the other rooms painted white. Each room takes 2 gallons of paint. Color paint comes in 1-gallon paint cans, and white paint comes in 3-gallon cans. How many cans of paint will Bill need for the whole house?"""
    # Define the number of bedrooms and other rooms
    bedrooms = 3
    other_rooms = bedrooms * 2

    # Calculate the total number of rooms in the house
    total_rooms = bedrooms + other_rooms

    # Calculate the total number of gallons of color paint needed
    color_paint_gallons = bedrooms

    # Calculate the total number of gallons of white paint needed
    white_paint_gallons = other_rooms

    # Calculate the total number of 1-gallon cans of color paint needed
    color_paint_cans = ceil(color_paint_gallons)

    # Calculate the total number of 3-gallon cans of white paint needed
    white_paint_cans = ceil(white_paint_gallons / 3)

    # Calculate the total number of cans of paint needed
    total_cans = color_paint_cans + white_paint_cans

    # Display the total number of cans of paint needed
    result = total_cans
    return result

print(solution())