def solution():
    """John gave his fiancee a $4000 ring on their engagement day, a $2000 car as a gift on their wedding day, and a diamond brace twice as expensive as the ring he gave her during the engagement. What's the worth of the presents John gave to her fiancee?"""
    engagement_ring = 4000
    wedding_car = 2000
    diamond_brace = engagement_ring * 2
    total_gifts = engagement_ring + wedding_car + diamond_brace
    result = total_gifts
    return result

print(solution())