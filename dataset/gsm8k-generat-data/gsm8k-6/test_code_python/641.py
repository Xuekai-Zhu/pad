def solution():
    meters_of_silk_per_dress = 5
    total_meters_of_silk_in_storage = 600
    meters_of_silk_given_to_friends = 20 * 5   # Alex has 5 friends, and each gets 20 meters of silk
    meters_of_silk_for_alex = total_meters_of_silk_in_storage - meters_of_silk_given_to_friends
    dresses_can_make = meters_of_silk_for_alex // meters_of_silk_per_dress
    result = dresses_can_make
    return result

print(solution())