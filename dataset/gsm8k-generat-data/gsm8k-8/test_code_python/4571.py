def solution():
    # Calculate Cisco's number of spots
    cisco_spots = (0.5 * 46) - 5

    # Calculate Granger's number of spots
    granger_spots = 5 * cisco_spots

    # Calculate the total number of spots
    total_spots = cisco_spots + granger_spots
    result = total_spots
    return result

print(solution())