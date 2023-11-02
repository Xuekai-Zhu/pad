def solution():
    # Calculate the total number of spots Jean has
    total_spots = 30 * 2  # Jean has 30 spots on her upper torso, so she has 60 spots in total

    # Calculate the number of spots on her back and hindquarters
    b_and_h_spots = total_spots / 3  # One-third of the spots are on her back and hindquarters

    # Calculate the number of spots on her sides
    side_spots = total_spots - 30 - b_and_h_spots  # Subtract the spots on upper torso and back/hindquarters

    result = side_spots
    return result

print(solution())