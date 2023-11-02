def solution():
    
    rover_spots = 46
    cisco_spots = (0.5 * rover_spots) - 5
    granger_spots = 5 * cisco_spots
    total_spots = cisco_spots + granger_spots
    result = total_spots
    return result

print(solution())