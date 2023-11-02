def solution():
    """Kevin holds the world record for eating the biggest quantity of hot wings in 8 minutes. He can eat 64 wings without stopping. Alan, a boy who loves hot wings, wants to beat Kevin's record. He is currently able to eat 5 hot wings per minute. How many more wings must he eat per minute to beat Kevin's record?"""
    kevin_record = 64
    kevin_time = 8
    kevin_speed = kevin_record / kevin_time
    alan_speed = 5
    additional_wings_per_minute = kevin_speed - alan_speed
    result = additional_wings_per_minute
    return result

print(solution())