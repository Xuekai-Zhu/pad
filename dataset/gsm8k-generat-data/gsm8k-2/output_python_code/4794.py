def solution():
    """James does chores around the class. There are 3 bedrooms, 1 living room, and 2 bathrooms to clean. The bedrooms each take 20 minutes to clean. The living room takes as long as the 3 bedrooms combined. The bathroom takes twice as long as the living room. He also cleans the outside which takes twice as long as cleaning the house. He splits the chores with his 2 siblings who are just as fast as him. How long, in hours, does he work?"""
    bedroom_time = 20 * 3
    living_room_time = bedroom_time * 3
    bathroom_time = living_room_time * 2
    house_time = bedroom_time + living_room_time + bathroom_time
    outside_time = house_time * 2
    total_time = (house_time + outside_time) / 3
    total_hours = total_time / 60
    result = total_hours
    return result

print(solution())