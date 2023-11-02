def solution():
    """Stella and Twinkle are filling up a truck with a capacity of 6000 stone blocks at the rate of 250 blocks per hour per person. They work for four hours and are then joined by 6 other people who also work at the same rate. How many hours did filling the truck take?"""
    blocks_to_fill = 6000
    blocks_per_hour = 250
    workers = 2
    hours = 4
    blocks_filled = blocks_per_hour * workers * hours
    extra_workers = 6
    extra_hours = (blocks_to_fill - blocks_filled) / (blocks_per_hour * extra_workers)
    total_hours = hours + extra_hours
    result = total_hours
    return result

print(solution())