def solution():
    # Calculate the number of spots Cisco has
    cisco_spots = (1/2) * 46 - 5

    # Calculate the number of spots Granger has
    granger_spots = 5 * cisco_spots

    # Calculate the total number of spots
    total_spots = cisco_spots + granger_spots

    result = total_spots
    return result

print(solution())