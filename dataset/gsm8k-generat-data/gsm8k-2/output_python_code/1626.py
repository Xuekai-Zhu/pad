def solution():
    """Grace is filling her pool in the backyard with a hose that sprays 50 gallons/hour. She waited for 3 hours but the pool wasn't full, so she decides to add another hose that sprays 70 gallons/hour, and after 2 more hours the pool is full. How much water can Grace’s pool contain?"""
    # Volume of water sprayed per hour by each hose
    hose1 = 50
    hose2 = 70

    # Time taken with just one hose
    time1 = 3

    # Time taken with both hoses
    time2 = 2

    # Let the volume of the pool be x gallons
    # Then, in the first 3 hours, only hose 1 was used
    # Hence, the amount filled in the pool during this period can be calculated as:
    volume_filled_by_hose1 = hose1 * time1

    # The remaining volume of the pool that needs to be filled is:
    remaining_volume = x - volume_filled_by_hose1

    # After that, both hoses are used for 2 more hours to fill the remaining volume
    # Let the volume of water filled by hose 1 during this period be y gallons
    # Then the volume of water filled by hose 2 will be (remaining_volume - y) gallons
    # Total volume filled in 2 hours = y * hose1 + (remaining_volume - y) * hose2
    # We want this to be equal to the remaining volume of the pool
    # Hence, we can solve for y as follows:
    y = remaining_volume / (hose1 + hose2) - (time1 + time2)

    # Therefore, the maximum volume of water that the pool can contain is:
    x = volume_filled_by_hose1 + y * hose1 + (remaining_volume - y) * hose2
    result = x
    return result

print(solution())