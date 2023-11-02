def solution():
    """Hannah fills her kids' stockings with 4 candy canes, 2 beanie babies and 1 book. If she has 3 kids, how many stocking stuffers does she buy total?"""
    candy_canes = 4
    beanie_babies = 2
    books = 1
    kids = 3
    total_stuffers = (candy_canes + beanie_babies + books) * kids
    result = total_stuffers
    return result

print(solution())