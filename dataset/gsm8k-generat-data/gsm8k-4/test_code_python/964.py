def solution():
    """Kevin holds the world record for eating the biggest quantity of hot wings in 8 minutes. He can eat 64 wings without stopping. Alan, a boy who loves hot wings, wants to beat Kevin's record. He is currently able to eat 5 hot wings per minute. How many more wings must he eat per minute to beat Kevin's record?"""
    # Define Kevin's record and Alan's current eating speed
    kevin_record = 64
    alan_speed = 5

    # Calculate the total number of wings Alan needs to eat to beat Kevin's record
    alan_record = kevin_record + 1

    # Calculate the time Alan needs to eat all the wings
    alan_time = alan_record / alan_speed

    # Calculate the number of wings Alan needs to eat per minute to beat Kevin's record
    alan_wings_per_minute = alan_record / 8

    # Calculate the difference in wings per minute between Alan's current speed and his new needed speed
    difference = alan_wings_per_minute - alan_speed

    result = difference
    return result

print(solution())