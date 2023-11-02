def solution():
    """Jean the jaguar has a beautiful fur coat containing a pattern of many rose-shaped spots, as unique as a human fingerprint.  Half of her spots are located on her upper torso, with one-third of the spots located on her back and hindquarters, and the remaining spots located on her sides.  If Jean has 30 spots on her upper torso, how many spots does she have located on her sides?"""
    
    # Define the number of spots on Jean's upper torso
    upper_torso_spots = 30
    
    # Calculate the total number of spots
    total_spots = upper_torso_spots * 2
    
    # Calculate the number of spots on Jean's back and hindquarters
    back_hindquarters_spots = total_spots // 3
    
    # Calculate the number of spots on Jean's sides
    side_spots = total_spots - upper_torso_spots - back_hindquarters_spots
    
    # Display the number of spots on Jean's sides
    result = side_spots
    return result

print(solution())