def solution():
    num_riverside_kids = 120
    num_westside_kids = 90
    num_mountaintop_kids = 50

    # Calculate the number of kids denied from Riverside High
    num_riverside_denied = 0.2 * num_riverside_kids

    # Calculate the number of kids denied from West Side High
    num_westside_denied = 0.7 * num_westside_kids

    # Calculate the number of kids denied from Mountaintop High
    num_mountaintop_denied = 0.5 * num_mountaintop_kids

    # Calculate the total number of kids denied
    total_denied = num_riverside_denied + num_westside_denied + num_mountaintop_denied

    # Calculate the total number of kids that got into the movie
    total_allowed = (num_riverside_kids + num_westside_kids + num_mountaintop_kids) - total_denied
    result = total_allowed
    return result

print(solution())