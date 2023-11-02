def solution():
    """Fern is checking IDs to get into an R-rated movie. She denied 20% of the 120 kids from Riverside High, 70% of the 90 kids from West Side High, and half the 50 kids from Mountaintop High. How many kids got into the movie?"""
    # Calculate the number of kids from Riverside High who got into the movie
    riverside_kids = 120 * 0.8

    # Calculate the number of kids from West Side High who got into the movie
    westside_kids = 90 * 0.3

    # Calculate the number of kids from Mountaintop High who got into the movie
    mountaintop_kids = 50 * 0.5

    # Calculate the total number of kids who got into the movie
    total_kids = riverside_kids + westside_kids + mountaintop_kids

    # return the result
    result = total_kids
    return result

print(solution())