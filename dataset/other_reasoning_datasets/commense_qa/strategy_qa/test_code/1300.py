def solution():
    # Define size of newborn kitten and Amtrak coach seat
    kitten_size = 7  # inches
    seat_length = 39  # inches
    seat_width = 23  # inches
    
    # Calculate area of coach seat
    seat_area = seat_length * seat_width
    
    # Calculate total area needed for three kittens
    kitten_area = kitten_size ** 2
    total_kitten_area = kitten_area * 3
    
    # Check if total kitten area is smaller than or equal to seat area
    if total_kitten_area <= seat_area:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())