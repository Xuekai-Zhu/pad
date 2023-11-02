def solution():
    """Granger has five times as many spots as his brother, Cisco. But Cisco has 5 less than half as many spots as his cousin, Rover. If Rover has 46 spots, how many spots do Granger and Cisco have combined?"""
    # Define the number of spots of Rover
    rover_spots = 46

    # Calculate the number of spots of Cisco
    cisco_spots = (rover_spots / 2) - 5

    # Calculate the number of spots of Granger
    granger_spots = cisco_spots * 5

    # Calculate the total number of spots
    total_spots = cisco_spots + granger_spots

    # Return the result
    result = total_spots
    return result

print(solution())