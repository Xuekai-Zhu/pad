def solution():
    # Calculate the percentage of ads that are not interesting but get blocked
    not_interesting_and_blocked = 80 * 0.2  
    # Calculate the percentage of ads that aren't interesting and don't get blocked
    not_interesting_and_not_blocked = 80 - not_interesting_and_blocked

    result = not_interesting_and_not_blocked
    return result

print(solution())