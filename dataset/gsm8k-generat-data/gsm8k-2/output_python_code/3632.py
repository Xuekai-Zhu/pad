def solution():
    """Marcy keeps a 2-liter bottle of water by her desk. She takes a sip every five minutes, and each sip is 40 ml. How many minutes does it take her to drink the whole bottle of water?"""
    bottle_size = 2000 # in ml
    sip_size = 40 
    time_per_sip = 5 
    total_sips = bottle_size / sip_size
    total_time_in_minutes = total_sips * time_per_sip
    result = total_time_in_minutes
    return result

print(solution())