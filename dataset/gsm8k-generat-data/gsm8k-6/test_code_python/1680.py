def solution():
    # Calculate the remaining number of candies in the bowl
    start_count = 349
    talitha_count = 108
    solomon_count = 153
    remaining_count = start_count - talitha_count - solomon_count
    result = remaining_count
    return result

print(solution())