def solution():
    # Calculate the number of remaining hotdogs Lisa needs to eat
    remaining_hotdogs = 75 - 20

    # Calculate the remaining time in minutes
    remaining_time = 10 / 2

    # Calculate the number of hotdogs Lisa needs to eat per minute to tie the record
    hotdogs_per_minute = remaining_hotdogs / remaining_time

    result = hotdogs_per_minute
    return result

print(solution())