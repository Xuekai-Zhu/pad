def solution():
    """James does chores around the class. There are 3 bedrooms, 1 living room, and 2 bathrooms to clean. The bedrooms each take 20 minutes to clean. The living room takes as long as the 3 bedrooms combined. The bathroom takes twice as long as the living room. He also cleans the outside which takes twice as long as cleaning the house. He splits the chores with his 2 siblings who are just as fast as him. How long, in hours, does he work?"""
    bedrooms = 3
    living_room = bedrooms * 3
    bathroom = living_room * 2
    outside = (bedrooms + living_room + bathroom) * 2
    total_minutes = (bedrooms * 20 + living_room + bathroom + outside) / 3
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())