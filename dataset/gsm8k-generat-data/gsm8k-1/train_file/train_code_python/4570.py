def solution():
    """Granger has five times as many spots as his brother, Cisco. But Cisco has 5 less than half as many spots as his cousin, Rover.
    If Rover has 46 spots, how many spots do Granger and Cisco have combined?"""
    rover_spots = 46
    cisco_spots = (rover_spots / 2) - 5
    granger_spots = cisco_spots * 5
    total_spots = cisco_spots + granger_spots
    result = total_spots
    return result

print(solution())