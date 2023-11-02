def solution():
    hunts_per_month = 6  # Jack goes hunting 6 times a month
    hunting_season = 0.25  # The hunting season lasts for 1 quarter of the year
    deers_caught_per_hunt = 2  # Jack catches 2 deer each time he goes hunting
    deer_weight = 600  # Each deer weighs 600 pounds
    weight_kept_ratio = 0.5  # Jack keeps half the weight of the deer he catches in a year

    # Calculate the total number of hunts Jack goes on in a year
    hunts_per_year = hunts_per_month * 12

    # Calculate the total number of deer Jack catches in a year
    total_deer_caught = hunts_per_year * deers_caught_per_hunt

    # Calculate the total weight of the deer Jack catches in a year
    total_weight = total_deer_caught * deer_weight

    # Calculate the weight of the deer Jack keeps in a year
    weight_kept = total_weight * weight_kept_ratio
    result = weight_kept
    return result

print(solution())