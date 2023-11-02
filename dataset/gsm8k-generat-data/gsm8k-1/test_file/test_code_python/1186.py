def solution():
    """A nurses’ station orders bandages in bulk packs of 50. On the first day, the nurses used 38 bandages and ordered one bulk pack of bandages. On the second day, they used ten fewer bandages. On the third day, they ordered two bulk packs of bandages and only used half a pack. They had 78 bandages left at the end of the third day. How many bandages did they start with on the first day?"""
    bandages_per_pack = 50
    first_day_usage = 38
    first_day_orders = 1
    second_day_usage = first_day_usage - 10
    second_day_orders = 0
    third_day_usage = bandages_per_pack / 2
    third_day_orders = 2
    starting_bandages = (first_day_orders + second_day_orders) * bandages_per_pack - first_day_usage - second_day_usage - third_day_usage + 78
    result = starting_bandages
    return result

print(solution())