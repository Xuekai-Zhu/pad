def solution():
    # Joey Chestnut ate 75 hotdogs in 10 minutes
    time_limit = 10
    joey_hotdogs = 75

    # Lisa has already eaten 20 hotdogs halfway through the time
    lisa_hotdogs = 20
    lisa_time = time_limit / 2

    # Calculate how many hotdogs Lisa needs to eat in the remaining time to tie the record
    hotdogs_left = joey_hotdogs - lisa_hotdogs
    time_left = time_limit - lisa_time
    hotdogs_per_minute = hotdogs_left / time_left
    result = hotdogs_per_minute
    return result

print(solution())