def solution():
    # Calculate how many kids were denied entry from each school
    denied_riverside = int(0.2 * 120)
    denied_westside = int(0.7 * 90)
    denied_mountain = int(0.5 * 50)

    # Calculate how many kids from each school were allowed entry
    allowed_riverside = 120 - denied_riverside
    allowed_westside = 90 - denied_westside
    allowed_mountain = 50 - denied_mountain

    # Calculate the total number of kids allowed entry
    total_allowed = allowed_riverside + allowed_westside + allowed_mountain
    result = total_allowed
    return result

print(solution())