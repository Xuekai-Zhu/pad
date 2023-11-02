def solution():
    num_spots_rover = 46

    # Calculate the number of spots Cisco has
    num_spots_cisco = (num_spots_rover / 2) - 5

    # Calculate the number of spots Granger has
    num_spots_granger = num_spots_cisco * 5

    # Calculate the total number of spots Cisco and Granger have combined
    total_spots = num_spots_cisco + num_spots_granger
    result = total_spots
    return result

print(solution())