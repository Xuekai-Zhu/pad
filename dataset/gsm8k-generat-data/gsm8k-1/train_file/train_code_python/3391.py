def solution():
    """At the museum, Bethany saw 4 times more still lifes than portraits. If she saw 80 paintings total, how many portraits did she see?"""
    total_paintings = 80
    still_lifes = 4
    portraits = total_paintings / (still_lifes + 1)
    result = portraits
    return result

print(solution())