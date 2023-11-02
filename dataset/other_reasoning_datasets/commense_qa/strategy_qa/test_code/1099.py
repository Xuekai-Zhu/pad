def solution():
    # Define city and monument locations
    dusseldorf_location = "Germany"
    stonehenge_location = "England"
    # Check if the two locations are the same
    if dusseldorf_location != stonehenge_location:
        result = "no"
    else:
        result = "cannot determine"
    return result

print(solution())