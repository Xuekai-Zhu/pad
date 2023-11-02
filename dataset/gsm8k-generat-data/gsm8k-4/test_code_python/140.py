def solution():
    """Fern is checking IDs to get into an R-rated movie. She denied 20% of the 120 kids from Riverside High, 70% of the 90 kids from West Side High, and half the 50 kids from Mountaintop High. How many kids got into the movie?"""
    # Define the number of kids from each high school
    riverside_kids = 120
    westside_kids = 90
    mountaintop_kids = 50

    # Calculate the number of kids denied entry from each high school
    denied_riverside = riverside_kids * 0.2
    denied_westside = westside_kids * 0.7
    denied_mountaintop = mountaintop_kids * 0.5

    # Calculate the number of kids that got into the movie from each high school
    accepted_riverside = riverside_kids - denied_riverside
    accepted_westside = westside_kids - denied_westside
    accepted_mountaintop = mountaintop_kids - denied_mountaintop

    # Calculate the total number of kids that got into the movie
    total_accepted = accepted_riverside + accepted_westside + accepted_mountaintop

    # Return the result
    result = total_accepted
    return result

print(solution())