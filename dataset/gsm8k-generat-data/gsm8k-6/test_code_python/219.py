def solution():
    # Calculate how many hotdogs Lisa needs to eat in the remaining 5 minutes
    remaining_time = 10 - 5  # halfway through the time, Lisa has 5 minutes left
    hotdogs_left = 75 - 20  # Lisa has already eaten 20 hotdogs
    hotdogs_per_minute = hotdogs_left / remaining_time  # calculate how many hotdogs Lisa needs to eat per minute to tie Joey Chestnut's record
    result = hotdogs_per_minute
    return result

print(solution())