def solution():
    # Calculate the total amount of hay harvested this year
    total_acres = 5 + 7  # the farmer added 7 acres of grass this year
    total_harvest = total_acres * 560  # the farmer harvested 560 bales of hay per month from 1 acre of grass

    # Calculate the total amount of hay the horses will consume from September 1st to December 31st
    total_days = 122  # from September 1st to December 31st
    total_hay_consumed = 9 * 3 * total_days  # 9 horses consuming 3 bales of hay per day for a total of 122 days

    # Calculate the amount of hay the farmer will have left at the end of December
    hay_left = total_harvest - total_hay_consumed
    result = hay_left
    return result

print(solution())