def solution():
    """Kevin holds the world record for eating the biggest quantity of hot wings in 8 minutes. He can eat 64 wings without stopping. Alan, a boy who loves hot wings, wants to beat Kevin's record. He is currently able to eat 5 hot wings per minute. How many more wings must he eat per minute to beat Kevin's record?"""
    kevin_record = 64
    time = 8
    alan_wings_per_min = 5
    alan_total_wings = alan_wings_per_min * (time + 1) # adding 1 minute for safety margin
    wings_needed_to_beat_kevin = kevin_record - alan_total_wings
    minutes_left = time + 1 # adding 1 minute for safety margin
    wings_per_minute_needed = wings_needed_to_beat_kevin / minutes_left
    result = wings_per_minute_needed
    return result

print(solution())