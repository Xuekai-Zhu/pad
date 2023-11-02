def solution():
    # Define the number of bedrooms
    num_bedrooms = 3

    # Calculate the number of other rooms as twice the number of bedrooms
    num_other_rooms = num_bedrooms * 2

    # Calculate the total number of rooms
    total_rooms = num_bedrooms + num_other_rooms

    # Calculate the total number of gallons of paint needed
    total_gallons = num_bedrooms + (num_other_rooms * 0)  # other rooms will be painted white
    total_gallons *= 2  # each room takes 2 gallons of paint

    # Calculate the number of 1-gallon cans of color paint needed
    color_cans = num_bedrooms
    
    # Calculate the number of 3-gallon cans of white paint needed
    white_cans = (total_gallons - num_bedrooms) // 3 + 1  # use integer division to round up to the nearest can

    # Calculate the total number of cans needed
    total_cans = color_cans + white_cans
    result = total_cans
    return result

print(solution())