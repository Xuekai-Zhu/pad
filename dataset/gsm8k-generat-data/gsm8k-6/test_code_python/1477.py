def solution():
    # Calculate the number of times Jack goes hunting during the hunting season
    num_hunting_trips = 6 * 3  # the hunting season is 1 quarter of the year, so Jack goes hunting for 3 months

    # Calculate the total weight of deer Jack catches in a year
    total_weight = num_hunting_trips * 2 * 600  # Jack catches 2 deers each time he goes hunting, and each deer weighs 600 pounds
    kept_weight = total_weight / 2  # Jack keeps half the weight of deer he catches in a year

    result = kept_weight
    return result

print(solution())