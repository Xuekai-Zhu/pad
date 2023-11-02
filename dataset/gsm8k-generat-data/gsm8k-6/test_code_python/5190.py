def solution():
    total_homes = 200  # total number of homes
    homes_distributed_1hr = 2/5 * total_homes  # number of homes distributed after 1 hour
    homes_remaining_after_1hr = total_homes - homes_distributed_1hr  # number of homes remaining after 1 hour
    homes_distributed_3hrs = homes_distributed_1hr + 0.6 * homes_remaining_after_1hr  # number of homes distributed after 3 hours
    homes_remaining = total_homes - homes_distributed_3hrs  # number of homes remaining to distribute newspapers
    result = homes_remaining
    return result

print(solution())