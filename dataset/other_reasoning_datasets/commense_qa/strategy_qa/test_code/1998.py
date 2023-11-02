def solution():
    # Define the locations and mode of transportation
    starting_location = "New England"
    destination = "Sainsbury's"
    mode_of_transportation = "drive"
    # Check if driving is a feasible mode of transportation
    if starting_location != "United Kingdom" and mode_of_transportation == "drive":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())