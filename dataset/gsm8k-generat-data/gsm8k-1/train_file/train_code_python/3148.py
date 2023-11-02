def solution():
    """Isaac cut his 30 meters ribbon into 6 equal parts. He then used 4 parts of the ribbon. How many meters of ribbon are not used?"""
    total_meters = 30
    parts = 6
    used_parts = 4
    meters_per_part = total_meters / parts
    unused_meters = (parts - used_parts) * meters_per_part
    result = unused_meters
    return result

print(solution())