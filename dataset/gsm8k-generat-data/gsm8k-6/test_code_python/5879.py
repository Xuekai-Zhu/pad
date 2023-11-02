def solution():
    # Calculate the total number of spots on Jean's back and hindquarters
    back_spots = (1/3) * 30 * 2  # one-third of the spots are located on her back and hindquarters, and she has two sides
    # Calculate the total number of spots on Jean's sides
    side_spots = (1/2 + 1/3) * 30  # half of the spots are located on her upper torso, and one-third of the spots are located on her back and hindquarters
    # Calculate the total number of spots on Jean
    total_spots = 30 + back_spots + side_spots
    # Calculate the number of spots located on Jean's sides
    side_spots = total_spots - 30 - back_spots
    result = side_spots
    return result

print(solution())