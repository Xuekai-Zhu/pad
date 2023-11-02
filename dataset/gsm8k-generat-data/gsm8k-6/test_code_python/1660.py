def solution():
    # Calculate the number of yellow papayas on Friday
    yellow_friday = 2
    # Calculate the number of yellow papayas on Sunday
    yellow_sunday = 2 * yellow_friday
    # Calculate the total number of papayas remaining on the tree
    remaining_papayas = 14 - yellow_friday - yellow_sunday
    result = remaining_papayas
    return result

print(solution())