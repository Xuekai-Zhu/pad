def solution():
    total_hotdogs = 75  # Joey Chestnut ate 75 hotdogs in 10 minutes
    time_remaining = 5  # Lisa has 5 minutes remaining to eat the hotdogs
    hotdogs_eaten_already = 20  # Lisa has already eaten 20 hotdogs

    # Calculate the number of hotdogs Lisa needs to eat per minute to tie Joey Chestnut's record
    hotdogs_per_minute = (total_hotdogs - hotdogs_eaten_already) / time_remaining
    result = hotdogs_per_minute
    return result

print(solution())