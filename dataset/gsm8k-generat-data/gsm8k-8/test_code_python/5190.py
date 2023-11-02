def solution():
    total_homes = 200
    homes_distributed_first_hour = 2/5 * total_homes
    homes_remaining_after_first_hour = total_homes - homes_distributed_first_hour

    homes_distributed_next_two_hours = 0.6 * homes_remaining_after_first_hour
    homes_remaining = homes_remaining_after_first_hour - homes_distributed_next_two_hours

    result = homes_remaining
    return result

print(solution())