def solution():
    # Calculate the total weight of the luggage the six people have
    total_luggage_weight = 6 * 5 * 50

    # Calculate the remaining weight allowance on the plane
    remaining_weight = 6000 - total_luggage_weight

    # Calculate the maximum number of additional bags the plane can hold at maximum weight
    additional_bags = remaining_weight // 50

    result = additional_bags
    return result

print(solution())