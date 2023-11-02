def solution():
    """James has 5 dozen boxes of matches.  Each box contains 20 matches.  How many matches does James have?"""
    # Define the number of dozens of boxes James has
    dozen_boxes = 5

    # Define the number of matches per box
    MATCHES_PER_BOX = 20

    # Calculate the total number of matches
    total_matches = dozen_boxes * 12 * MATCHES_PER_BOX

    # Display the total number of matches
    result = total_matches
    return result

print(solution())