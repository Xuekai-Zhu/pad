def solution():
    # Calculate the number of expected yam buyers
    expected_yam_buyers = 375 / 3

    # Calculate the number of packages needed
    packages_needed = expected_yam_buyers

    # Calculate the number of bulk boxes needed
    bulk_boxes_needed = packages_needed / 25

    # Round up to the nearest whole number of bulk boxes
    bulk_boxes_needed = math.ceil(bulk_boxes_needed)

    result = bulk_boxes_needed
    return result

print(solution())