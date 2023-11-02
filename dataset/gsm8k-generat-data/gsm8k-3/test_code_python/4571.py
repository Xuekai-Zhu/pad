def solution():
    """Granger has five times as many spots as his brother, Cisco. But Cisco has 5 less than half as many spots as his cousin, Rover. If Rover has 46 spots, how many spots do Granger and Cisco have combined?"""
    # Define the number of spots that Rover has
    rover_spots = 46

    # Calculate the number of spots that Cisco has
    cisco_spots = (rover_spots / 2) - 5

    # Calculate the number of spots that Granger has
    granger_spots = 5 * cisco_spots

    # Calculate the total number of spots
    total_spots = cisco_spots + granger_spots

    # Display the total number of spots
    result = total_spots
    return result

print(solution())