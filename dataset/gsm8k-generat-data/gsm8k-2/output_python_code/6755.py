def solution():
    """John gave his fiancee a $4000 ring on their engagement day, a $2000 car as a gift on their wedding day, and a diamond brace twice as expensive as the ring he gave her during the engagement. What's the worth of the presents John gave to her fiancee?"""
    ring_price = 4000
    car_price = 2000
    diamond_brace_price = 2 * ring_price
    total_price = ring_price + car_price + diamond_brace_price
    result = total_price
    return result

print(solution())