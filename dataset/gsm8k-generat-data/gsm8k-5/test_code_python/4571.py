def solution():
    rover_spots = 46  # Rover has 46 spots
    cisco_spots = (0.5 * rover_spots) - 5  # Cisco has 5 less than half as many spots as Rover
    granger_spots = 5 * cisco_spots  # Granger has five times as many spots as Cisco

    # Calculate the total spots of Granger and Cisco combined
    total_spots = cisco_spots + granger_spots
    result = total_spots
    return result

print(solution())