def solution():
    """Between them, Mark and Sarah have 24 traffic tickets. Mark has twice as many parking tickets as Sarah, and they each have an equal number of speeding tickets. If Sarah has 6 speeding tickets, how many parking tickets does Mark have?"""
    sarah_speeding = 6
    mark_speeding = sarah_speeding
    mark_parking = 2 * (24 - sarah_speeding - mark_speeding) / 3
    result = mark_parking
    return result

print(solution())