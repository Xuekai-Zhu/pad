def solution():
    # Calculate the number of kids who were denied entry
    denied_riverside = 0.2 * 120
    denied_westside = 0.7 * 90
    denied_mountaintop = 0.5 * 50
    total_denied = denied_riverside + denied_westside + denied_mountaintop

    # Calculate the number of kids who got into the movie
    total_kids = 120 + 90 + 50
    admitted_kids = total_kids - total_denied
    result = admitted_kids
    return result

print(solution())