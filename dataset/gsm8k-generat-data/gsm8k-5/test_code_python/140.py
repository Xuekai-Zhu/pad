def solution():
    # Calculate number of kids denied from each school
    denied_riverside = 0.20 * 120
    denied_westside = 0.70 * 90
    denied_mountaintop = 0.50 * 50

    # Calculate number of kids allowed from each school
    allowed_riverside = 120 - denied_riverside
    allowed_westside = 90 - denied_westside
    allowed_mountaintop = 50 - denied_mountaintop

    # Calculate total number of kids allowed in the movie
    total_allowed = allowed_riverside + allowed_westside + allowed_mountaintop
    result = total_allowed
    return result

print(solution())