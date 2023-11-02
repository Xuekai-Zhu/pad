def solution():
    num_peaches = 18
    num_ripe = 4
    num_ripe_per_day = 2
    num_eaten_on_third_day = 3
    num_days = 5

    # Calculate the total number of ripe peaches after five days
    total_ripe_peaches = num_ripe + (num_ripe_per_day * (num_days - 1)) - num_eaten_on_third_day

    # Calculate the number of unripe peaches remaining in the bowl
    num_unripe_peaches = num_peaches - total_ripe_peaches

    # Calculate the difference between the number of ripe and unripe peaches
    diff = total_ripe_peaches - num_unripe_peaches
    result = diff
    return result

print(solution())