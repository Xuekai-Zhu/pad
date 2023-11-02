def solution():
    # Calculate the total number of spots
    total_spots = 30 / 0.5

    # Calculate the number of spots on Jean's back and hindquarters
    back_spots = total_spots * (1/3)

    # Calculate the number of spots on Jean's sides
    side_spots = total_spots - 30 - back_spots

    result = side_spots
    return result

print(solution())