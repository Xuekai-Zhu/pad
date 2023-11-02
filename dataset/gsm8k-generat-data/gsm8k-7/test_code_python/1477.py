def solution():
    num_hunting_per_month = 6
    months_in_quarter = 3
    deer_caught_per_hunting = 2
    deer_weight = 600
    deer_kept_fraction = 0.5

    # Calculate the total number of hunting trips during the hunting season (1 quarter)
    total_hunting_trips = num_hunting_per_month * months_in_quarter

    # Calculate the total weight of deer caught during the hunting season
    total_deer_weight = total_hunting_trips * deer_caught_per_hunting * deer_weight

    # Calculate the weight of deer that Jack decides to keep
    deer_kept_weight = total_deer_weight * deer_kept_fraction
    result = deer_kept_weight
    return result

print(solution())