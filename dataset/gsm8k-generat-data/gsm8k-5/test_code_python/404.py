def solution():
    # Calculate the total number of bales of hay harvested per month from the expanded farm
    bales_per_month = (560/5) * 12  # 560 bales from 5 acres per month, so (560/5) bales from 1 acre per month. Multiply by 12 for the expanded farm.

    # Calculate the total number of bales of hay harvested from September to December
    harvest_time = 4  # The farmer harvests hay for 4 months
    total_harvest = bales_per_month * harvest_time

    # Calculate the total number of bales of hay consumed by the horses
    total_hay_consumed = 9 * 3 * 122  # 3 bales per day per horse, for 122 days from September to December

    # Calculate the number of bales of hay left
    hay_left = total_harvest - total_hay_consumed
    result = hay_left
    return result

print(solution())