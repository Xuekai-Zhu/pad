def solution():
    num_bedrooms = 3  # The house has 3 bedrooms
    num_other_rooms = 2*num_bedrooms  # The house has twice as many other rooms as bedrooms
    num_rooms = num_bedrooms + num_other_rooms  # Total number of rooms in the house
    gallons_per_room = 2  # Each room takes 2 gallons of paint

    # Calculate the total number of gallons of color paint needed
    num_gallons_color_paint = num_bedrooms * gallons_per_room

    # Calculate the total number of gallons of white paint needed
    num_gallons_white_paint = num_other_rooms * gallons_per_room / 3

    # Calculate the total number of cans of paint needed, rounding up to the nearest whole number
    total_cans_paint = round(num_gallons_color_paint + num_gallons_white_paint)

    result = total_cans_paint
    return result

print(solution())