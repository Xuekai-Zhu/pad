def solution():
    kibble_cups_per_day = 2
    kibble_cups_given_by_mary = 2
    kibble_cups_given_by_frank = 3
    total_kibble_cups = kibble_cups_per_day + kibble_cups_given_by_mary + kibble_cups_given_by_frank
    remaining_kibble_cups = 12 - total_kibble_cups
    result = remaining_kibble_cups
    return result

print(solution())